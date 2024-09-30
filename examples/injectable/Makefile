CC = gcc
CFLAGS = -Wall -O2 -Wno-unused-result
PROGS = loggable loggable2 loggable3
SRC_FILES = loggable.c loggable2.c loggable3.c
FLAG_FILE = /tmp/loggable
LEAK_FILE = leak.txt
FAKE_PRG = tee
PORT = 1337

.PHONY: all clean patches exploit1 exploit2

# Default target
all: $(PROGS) $(FLAG_FILE)

# Compile the vulnerable version
loggable: loggable.c
	$(CC) $(CFLAGS) -o $@ $<

# Compile the first patched version
loggable2: loggable2.c
	$(CC) $(CFLAGS) -o $@ $<

# Compile the final patched version
loggable3: loggable3.c
	$(CC) $(CFLAGS) -o $@ $<

# Generate the patches
patches: loggable.c loggable2.c loggable3.c
	-@diff -u loggable.c loggable2.c > patch1.diff
	-@diff -u loggable2.c loggable3.c > patch2.diff

$(FLAG_FILE):
	echo "Secret: AllYourPasswordsAreBelongToUs" > ${FLAG_FILE}

exploit1: exploit_loggable.py
	python3 exploit_loggable.py
	cat $(LEAK_FILE)

exploit2: exploit_loggable2.py
	python3 exploit_loggable2.py
	cat $(LEAK_FILE)

run1:
	socat TCP-LISTEN:${PORT},reuseaddr,fork EXEC:./loggable,pipes

run2:
	socat TCP-LISTEN:${PORT},reuseaddr,fork EXEC:./loggable2,pipes

run3:
	socat TCP-LISTEN:${PORT},reuseaddr,fork EXEC:./loggable3,pipes


# Clean up build artifacts
clean:
	rm -f $(PROGS) *.o patch1.diff patch2.diff $(FLAG_FILE) $(LEAK_FILE) $(FAKE_PRG)