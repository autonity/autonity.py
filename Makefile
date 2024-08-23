VERSION = $(shell cat AUTONITY_VERSION)
AUTONITY = build/autonity
ABIDIR = $(AUTONITY)/params/generated
OUTDIR = autonity/contracts
ABIGEN = hatch run generate:pyabigen \
			--srcdir $(AUTONITY)/autonity/solidity/contracts \
			--version $(VERSION)

all: $(OUTDIR)/accountability.py \
	 $(OUTDIR)/acu.py \
	 $(OUTDIR)/autonity.py \
	 $(OUTDIR)/inflation_controller.py \
	 $(OUTDIR)/liquid.py \
	 $(OUTDIR)/non_stakable_vesting.py \
	 $(OUTDIR)/oracle.py \
	 $(OUTDIR)/stabilization.py \
	 $(OUTDIR)/supply_control.py \
	 $(OUTDIR)/upgrade_manager.py

$(OUTDIR)/accountability.py: $(ABIDIR)/Accountability.abi
	$(ABIGEN) --exclude distributeRewards,finalize,setEpochPeriod $< >$@

$(OUTDIR)/acu.py: $(ABIDIR)/ACU.abi
	$(ABIGEN) --exclude setOperator,setOracle,update $< >$@

$(OUTDIR)/autonity.py: $(ABIDIR)/Autonity.abi
	$(ABIGEN) --exclude computeCommittee,finalize,finalizeInitialization $< >$@

$(OUTDIR)/inflation_controller.py: $(ABIDIR)/InflationController.abi
	$(ABIGEN) $< >$@

$(OUTDIR)/liquid.py: $(ABIDIR)/Liquid.abi
	$(ABIGEN) --exclude burn,lock,mint,redistribute,setCommissionRate,unlock $< >$@

$(OUTDIR)/non_stakable_vesting.py: $(ABIDIR)/NonStakableVesting.abi
	$(ABIGEN) --exclude unlockTokens $< >$@

$(OUTDIR)/oracle.py: $(ABIDIR)/Oracle.abi
	$(ABIGEN) --exclude finalize,setOperator,setVoters $< >$@

$(OUTDIR)/stabilization.py: $(ABIDIR)/Stabilization.abi
	$(ABIGEN) --exclude setOperator,setOracle $< >$@

$(OUTDIR)/supply_control.py: $(ABIDIR)/SupplyControl.abi
	$(ABIGEN) --exclude setOperator $< >$@

$(OUTDIR)/upgrade_manager.py: $(ABIDIR)/UpgradeManager.abi
	$(ABIGEN) --exclude setOperator $< >$@

$(ABIDIR)/%.abi: $(AUTONITY) AUTONITY_VERSION
	cd $< && \
	git fetch origin && \
	git checkout $(VERSION) && \
	make contracts

$(AUTONITY):
	git clone git@github.com:autonity/autonity.git $@

clean:
	rm -rf $(AUTONITY)

.PHONY = clean
