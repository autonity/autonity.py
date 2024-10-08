VERSION := $(shell cat AUTONITY_VERSION)
AUTONITY := build/autonity
ABIDIR := $(AUTONITY)/params/generated
SRCDIR := $(AUTONITY)/autonity/solidity/contracts
OUTDIR := autonity/contracts

abigen = hatch run generate:pyabigen \
	--version $(VERSION) \
	--src $(word 1,$(1)) \
	--devdoc $(word 2,$(1)) \
	--userdoc $(word 3,$(1)) \
	$(word 4,$(1))
gentargets = $(shell find $(SRCDIR) -name $(1).sol) $(addprefix $(ABIDIR)/$(1),.docdev .docuser .abi)

all: $(OUTDIR)/accountability.py \
	 $(OUTDIR)/acu.py \
	 $(OUTDIR)/autonity.py \
	 $(OUTDIR)/ierc20.py \
	 $(OUTDIR)/inflation_controller.py \
	 $(OUTDIR)/liquid.py \
	 $(OUTDIR)/non_stakable_vesting.py \
	 $(OUTDIR)/oracle.py \
	 $(OUTDIR)/stabilization.py \
	 $(OUTDIR)/supply_control.py \
	 $(OUTDIR)/upgrade_manager.py

$(OUTDIR)/accountability.py: $(call gentargets,Accountability)
	$(call abigen,$^) --exclude distributeRewards,finalize,handleEvent,setEpochPeriod >$@

$(OUTDIR)/acu.py: $(call gentargets,ACU)
	$(call abigen,$^) --exclude setOperator,setOracle,update >$@

$(OUTDIR)/autonity.py: $(call gentargets,Autonity)
	$(call abigen,$^) --exclude computeCommittee,finalize,finalizeInitialization,updateValidatorAndTransferSlashedFunds >$@

$(OUTDIR)/ierc20.py: $(call gentargets,IERC20)
	$(call abigen,$^) >$@

$(OUTDIR)/inflation_controller.py: $(call gentargets,InflationController)
	$(call abigen,$^) >$@

$(OUTDIR)/liquid.py: $(call gentargets,Liquid)
	$(call abigen,$^) --exclude burn,lock,mint,redistribute,setCommissionRate,unlock >$@

$(OUTDIR)/non_stakable_vesting.py: $(call gentargets,NonStakableVesting)
	$(call abigen,$^) --exclude unlockTokens >$@

$(OUTDIR)/oracle.py: $(call gentargets,Oracle)
	$(call abigen,$^) --exclude finalize,setOperator,setVoters,vote >$@

$(OUTDIR)/stabilization.py: $(call gentargets,Stabilization)
	$(call abigen,$^) --exclude setOperator,setOracle >$@

$(OUTDIR)/supply_control.py: $(call gentargets,SupplyControl)
	$(call abigen,$^) --exclude burn,mint,setOperator >$@

$(OUTDIR)/upgrade_manager.py: $(call gentargets,UpgradeManager)
	$(call abigen,$^) --exclude setOperator >$@

$(ABIDIR)/%.abi: $(AUTONITY) AUTONITY_VERSION
	cd $< && \
	git fetch origin && \
	git checkout $(VERSION) && \
	make contracts

# This recipe can be removed after https://github.com/autonity/autonity/pull/1035 is released
$(ABIDIR)/%.docuser $(ABIDIR)/%.docdev: $(ABIDIR)/%.abi
	$(AUTONITY)/build/bin/solc_static_linux_v0.8.21 \
		--overwrite --userdoc --devdoc -o $(ABIDIR) \
		$$(find $(AUTONITY)/autonity/solidity/contracts -name $(basename $(notdir $<)).sol)

$(AUTONITY):
	git clone git@github.com:autonity/autonity.git $@

clean:
	rm -rf $(AUTONITY)

.PHONY = clean
