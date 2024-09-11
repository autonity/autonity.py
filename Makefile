VERSION := $(shell cat AUTONITY_VERSION)
AUTONITY := build/autonity
ABIDIR := $(AUTONITY)/params/generated
SRCDIR := $(AUTONITY)/autonity/solidity/contracts
OUTDIR := autonity/contracts
BINDINGS := \
	$(OUTDIR)/accountability.py \
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

gentargets = $(shell find $(SRCDIR) -name $(1).sol) $(addprefix $(ABIDIR)/$(1),.docdev .docuser .abi)

all: $(BINDINGS)

$(OUTDIR)/accountability.py: $(call gentargets,Accountability)
$(OUTDIR)/acu.py: $(call gentargets,ACU)
$(OUTDIR)/autonity.py: $(call gentargets,Autonity)
$(OUTDIR)/ierc20.py: $(call gentargets,IERC20)
$(OUTDIR)/inflation_controller.py: $(call gentargets,InflationController)
$(OUTDIR)/liquid.py: $(call gentargets,Liquid)
$(OUTDIR)/non_stakable_vesting.py: $(call gentargets,NonStakableVesting)
$(OUTDIR)/oracle.py: $(call gentargets,Oracle)
$(OUTDIR)/stabilization.py: $(call gentargets,Stabilization)
$(OUTDIR)/supply_control.py: $(call gentargets,SupplyControl)
$(OUTDIR)/upgrade_manager.py: $(call gentargets,UpgradeManager)

$(BINDINGS):
	hatch run generate:pyabigen \
		--version $(VERSION) \
		--src $(word 1,$^) \
		--devdoc $(word 2,$^) \
		--userdoc $(word 3,$^) \
		$(word 4,$^) >$@

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
