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
	$(ABIGEN) \
		--address 0x5a443704dd4B594B382c22a083e2BD3090A6feF3 \
		--exclude distributeRewards,finalize,setEpochPeriod \
		$< >$@

$(OUTDIR)/acu.py: $(ABIDIR)/ACU.abi
	$(ABIGEN) \
		--address 0x8Be503bcdEd90ED42Eff31f56199399B2b0154CA \
		--exclude setOperator,setOracle,update \
		$< >$@

$(OUTDIR)/autonity.py: $(ABIDIR)/Autonity.abi
	$(ABIGEN) \
		--address 0xBd770416a3345F91E4B34576cb804a576fa48EB1 \
		--exclude computeCommittee,finalize,finalizeInitialization \
		$< >$@

$(OUTDIR)/inflation_controller.py: $(ABIDIR)/InflationController.abi
	$(ABIGEN) \
		--address 0x3BB898B4Bbe24f68A4e9bE46cFE72D1787FD74F4 \
		$< >$@

$(OUTDIR)/liquid.py: $(ABIDIR)/Liquid.abi
	$(ABIGEN) \
		--exclude burn,lock,mint,redistribute,setCommissionRate,unlock \
		$< >$@

$(OUTDIR)/non_stakable_vesting.py: $(ABIDIR)/NonStakableVesting.abi
	$(ABIGEN) \
		--address 0x6901F7206A34E441Ac5020b5fB53598A65547A23 \
		--exclude unlockTokens \
		$< >$@

$(OUTDIR)/oracle.py: $(ABIDIR)/Oracle.abi
	$(ABIGEN) \
		--address 0x47e9Fbef8C83A1714F1951F142132E6e90F5fa5D \
		--exclude finalize,setOperator,setVoters \
		$< >$@

$(OUTDIR)/stabilization.py: $(ABIDIR)/Stabilization.abi
	$(ABIGEN) \
		--address 0x29b2440db4A256B0c1E6d3B4CDcaA68E2440A08f \
		--exclude setOperator,setOracle \
		$< >$@

$(OUTDIR)/supply_control.py: $(ABIDIR)/SupplyControl.abi
	$(ABIGEN) \
		--address 0x47c5e40890bcE4a473A49D7501808b9633F29782 \
		--exclude setOperator \
		$< >$@

$(OUTDIR)/upgrade_manager.py: $(ABIDIR)/UpgradeManager.abi
	$(ABIGEN) \
		--address 0x3C368B86AF00565Df7a3897Cfa9195B9434A59f9 \
		--exclude setOperator \
		$< >$@

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
