VERSION := $(shell cat AUTONITY_VERSION)
AUTONITY := build/autonity
ABIDIR := $(AUTONITY)/params/generated
OUTDIR := autonity/contracts
ABIGEN = hatch run generate:pyabigen \
			--srcdir $(AUTONITY)/autonity/solidity/contracts \
			--version $(VERSION) \
			--userdoc $(word 2,$(1)) \
			--devdoc $(word 3,$(1)) \
			$(word 1,$(1))

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

$(OUTDIR)/accountability.py: $(addprefix $(ABIDIR)/Accountability,.abi .docuser .docdev)
	$(call ABIGEN,$^) --exclude distributeRewards,finalize,setEpochPeriod >$@

$(OUTDIR)/acu.py: $(addprefix $(ABIDIR)/ACU,.abi .docuser .docdev)
	$(call ABIGEN,$^) --exclude setOperator,setOracle,update >$@

$(OUTDIR)/autonity.py: $(addprefix $(ABIDIR)/Autonity,.abi .docuser .docdev)
	$(call ABIGEN,$^) --exclude computeCommittee,finalize,finalizeInitialization >$@

$(OUTDIR)/ierc20.py: $(addprefix $(ABIDIR)/IERC20,.abi .docuser .docdev)
	$(call ABIGEN,$^) >$@

$(OUTDIR)/inflation_controller.py: $(addprefix $(ABIDIR)/InflationController,.abi .docuser .docdev)
	$(call ABIGEN,$^) >$@

$(OUTDIR)/liquid.py: $(addprefix $(ABIDIR)/Liquid,.abi .docuser .docdev)
	$(call ABIGEN,$^) --exclude burn,lock,mint,redistribute,setCommissionRate,unlock >$@

$(OUTDIR)/non_stakable_vesting.py: $(addprefix $(ABIDIR)/NonStakableVesting,.abi .docuser .docdev)
	$(call ABIGEN,$^) --exclude unlockTokens >$@

$(OUTDIR)/oracle.py: $(addprefix $(ABIDIR)/Oracle,.abi .docuser .docdev)
	$(call ABIGEN,$^) --exclude finalize,setOperator,setVoters >$@

$(OUTDIR)/stabilization.py: $(addprefix $(ABIDIR)/Stabilization,.abi .docuser .docdev)
	$(call ABIGEN,$^) --exclude setOperator,setOracle >$@

$(OUTDIR)/supply_control.py: $(addprefix $(ABIDIR)/SupplyControl,.abi .docuser .docdev)
	$(call ABIGEN,$^) --exclude setOperator >$@

$(OUTDIR)/upgrade_manager.py: $(addprefix $(ABIDIR)/UpgradeManager,.abi .docuser .docdev)
	$(call ABIGEN,$^) --exclude setOperator >$@

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
