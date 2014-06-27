
COMPILER=../../PASM/pasm -b 
SOURCES=other.p \
		blue.p \
		red.p \
		green.p \
		orange.p

OBJECTS=$(SOURCES:.p=.bin)
.PHONY: clean all

all: $(OBJECTS)
	@echo "Finished building PRU binaries!"

%.bin: %.p
	@echo "Building $<"
	$(COMPILER) -b $<

clean: 
	rm -rf $(OBJECTS)


