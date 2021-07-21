IPC=./ipc_dir
TRU=./truth
CUR=./current
DB=test_db.ciphart

NSA       =../nsa -i $(IPC)
NSA_CREATE=$(NSA) create -s -d $(CUR)/$(DB)
NSA_START =$(NSA) start -s -d $(CUR)/$(DB) &
NSA_STOP  =$(NSA) stop
NSA_CHPASS=$(NSA) chpass -s
NSA_ADD   =$(NSA) add -s
NSA_DEL   =$(NSA) del
NSA_MOD   =$(NSA) mod -s
NSA_DO    =$(NSA) do
NSA_LS    =$(NSA) ls
NSA_REVERT=$(NSA) revert
NSA_COMMIT=$(NSA) commit

PASS     =echo    "lol"
PASS2    =echo -e "lol\nlol"
PASS_NEW =echo    "rofl"
PASS_NEW2=echo -e "rofl\nrofl"
PASS_USR =echo -e "lel\nlel"

DEC=ciphart -dks -i $(CUR)/$(DB)
CLN=python ./striptimestamps.py
DIFF=diff --color=always -u

all: test

.PHONY: test
test: clean
	# prepare tests
	mkdir -p $(CUR) $(IPC)
	# test docs
	$(NSA) -h > $(CUR)/-h
	$(NSA) -v > $(CUR)/-v
	$(DIFF)     $(TRU)/-h $(CUR)/-h
	$(DIFF)     $(TRU)/-v $(CUR)/-v
	# test create
	$(PASS2) | $(NSA_CREATE)
	$(PASS) | $(DEC) > $(CUR)/$(DB).create.str
	$(CLN) $(CUR)/$(DB).create.str > $(CUR)/$(DB).create.str.cln
	$(DIFF) $(TRU)/$(DB).create.str.cln $(CUR)/$(DB).create.str.cln
	# test start
	$(PASS) | $(NSA_START)
	sleep 5
	# test add
	$(NSA_ADD) -t tag1 tag2 -n "oy vey" -f $(TRU)/keyfile
	$(NSA_ADD) -t test asd dea s
	$(NSA_ADD) -t test
	$(PASS_USR) | $(NSA_ADD) -t asdfa lel -m
	$(NSA_COMMIT)
	$(PASS) | $(DEC) > $(CUR)/$(DB).add.str
	$(CLN) $(CUR)/$(DB).add.str > $(CUR)/$(DB).add.str.cln
	$(DIFF) $(TRU)/$(DB).add.str.cln $(CUR)/$(DB).add.str.cln
	# test del
	$(NSA_DEL) test
	$(NSA_COMMIT)
	$(PASS) | $(DEC) > $(CUR)/$(DB).del.str
	$(CLN) $(CUR)/$(DB).del.str > $(CUR)/$(DB).del.str.cln
	$(DIFF) $(TRU)/$(DB).del.str.cln $(CUR)/$(DB).del.str.cln
	# test mod
	$(NSA_MOD) t t -u barak -r https://mossad.gov.il
	$(NSA_MOD) t d -f $(TRU)/keyfile
	$(PASS_USR) | $(NSA_MOD) t t -m
	$(NSA_COMMIT)
	$(PASS) | $(DEC) > $(CUR)/$(DB).mod.str
	$(CLN) $(CUR)/$(DB).mod.str > $(CUR)/$(DB).mod.str.cln
	$(DIFF) $(TRU)/$(DB).mod.str.cln $(CUR)/$(DB).mod.str.cln
	# test do
	$(NSA_DO) t t -c k > $(CUR)/keyfile-t_t
	$(NSA_DO) t d -c k > $(CUR)/keyfile-t_d
	$(DIFF) $(TRU)/keyfile $(CUR)/keyfile-t_t
	$(DIFF) $(TRU)/keyfile $(CUR)/keyfile-t_d
	# test ls
	$(NSA_LS)
	# test chpass
	$(PASS_NEW2) | $(NSA_CHPASS)
	$(NSA_COMMIT)
	$(NSA_STOP)
	$(PASS_NEW) | $(NSA_START)
	sleep 5
	# test stop
	$(NSA_STOP)

.PHONY: clean
clean:
	# clean
	rm -rf $(CUR) $(IPC)
