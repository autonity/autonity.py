VERSION := $(shell cat AUTONITY_VERSION)
AUTONITY_DIR := build/autonity
AUTONITY_BIN := $(AUTONITY_DIR)/build/bin/autonity
ABIDIR := $(AUTONITY_DIR)/params/generated
SRCDIR := $(AUTONITY_DIR)/autonity/solidity/contracts
OUTDIR := autonity/contracts

abigen = hatch run generate:pyabigen \
	--version $(VERSION) \
	--src $(word 1,$(1)) \
	--devdoc $(word 2,$(1)) \
	--userdoc $(word 3,$(1)) \
	$(word 4,$(1))

gentargets = $(shell find $(SRCDIR) -name $(1).sol) \
	$(addprefix $(ABIDIR)/$(1),.docdev .docuser .abi) \
	pyproject.toml

all: $(OUTDIR)/accountability.py \
	 $(OUTDIR)/acu.py \
	 $(OUTDIR)/autonity.py \
	 $(OUTDIR)/inflation_controller.py \
	 $(OUTDIR)/liquid_logic.py \
	 $(OUTDIR)/omission_accountability.py \
	 $(OUTDIR)/oracle.py \
	 $(OUTDIR)/stabilization.py \
	 $(OUTDIR)/supply_control.py \
	 $(OUTDIR)/upgrade_manager.py

$(OUTDIR)/accountability.py: $(call gentargets,Accountability)
	$(call abigen,$^) --exclude distributeRewards,finalize,handleAccusation,handleEvent,handleInnocenceProof,handleMisbehaviour,setEpochPeriod >$@

$(OUTDIR)/acu.py: $(call gentargets,ACU)
	$(call abigen,$^) --exclude setOperator,setOracle,update >$@

$(OUTDIR)/autonity.py: $(call gentargets,Autonity)
	$(call abigen,$^) --exclude autobond,computeCommittee,finalize,finalizeInitialization,jail,jailbound,slash,slashAndJail >$@

$(OUTDIR)/inflation_controller.py: $(call gentargets,InflationController)
	$(call abigen,$^) >$@

$(OUTDIR)/liquid_logic.py: $(call gentargets,LiquidLogic)
	$(call abigen,$^) --exclude burn,lock,mint,redistribute,setCommissionRate,unlock >$@

$(OUTDIR)/omission_accountability.py: $(call gentargets,OmissionAccountability)
	$(call abigen,$^) --exclude finalize,setCommittee,setEpochBlock,setOperator >$@

$(OUTDIR)/oracle.py: $(call gentargets,Oracle)
	$(call abigen,$^) --exclude finalize,setOperator,setVoters,vote >$@

$(OUTDIR)/stabilization.py: $(call gentargets,Stabilization)
	$(call abigen,$^) --exclude setOperator,setOracle >$@

$(OUTDIR)/supply_control.py: $(call gentargets,SupplyControl)
	$(call abigen,$^) --exclude burn,mint,setOperator >$@

$(OUTDIR)/upgrade_manager.py: $(call gentargets,UpgradeManager)
	$(call abigen,$^) --exclude setOperator >$@

$(ABIDIR)/%.abi $(ABIDIR)/%.docdev $(ABIDIR)/%.docuser: $(AUTONITY_DIR) AUTONITY_VERSION
	cd $< && \
	git fetch origin && \
	git checkout -d $(VERSION) && \
	make contracts

$(AUTONITY_BIN): $(AUTONITY_DIR) AUTONITY_VERSION
	cd $< && \
	git fetch origin && \
	git checkout -d $(VERSION) && \
	make autonity

$(AUTONITY_DIR):
	git clone git@github.com:autonity/autonity.git $@

autonity: $(AUTONITY_BIN)

clean:
	rm -rf $(AUTONITY_DIR)

.PHONY = autonity clean
