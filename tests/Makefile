IPC=./ipc_dir
TRU=./truth
CUR=./current
DB=test_db

NSA       =../nsa -i $(IPC)
NSA_CREATE=$(NSA) create -s -d $(CUR)/$(DB)
NSA_START =$(NSA) start -s -d $(CUR)/$(DB) &
NSA_STOP  =$(NSA) stop
NSA_CHPASS=$(NSA) chpass -s
NSA_ADD   =$(NSA) add -s
NSA_DEL   =$(NSA) del
NSA_MOD   =$(NSA) mod -s
NSA_DIFF  =$(NSA) diff
NSA_DROP  =$(NSA) drop
NSA_COMMIT=$(NSA) commit
NSA_DO    =$(NSA) do
NSA_LS    =$(NSA) ls
NSA_REVERT=$(NSA) revert
NSA_COMMIT=$(NSA) commit

PASS     =echo -n  "lol"
PASS2    =echo -ne "lol\nlol"
PASS_NEW =echo -n  "rofl"
PASS_NEW2=echo -ne "rofl\nrofl"
PASS_USR =echo -ne "lel\nlel"

KDF=argon2 nsapasssalt -d -k 1048576 -p 4 -t 20 -r
DEC=$(KDF) | openssl enc -chacha20 -in=$(CUR)/$(DB) -d -kfile=- -iter=1
CLN=python ./striptimestamps.py
DIFF=diff --color=always -u

GR="\033[1;32m"
NC="\033[0m"
PREFIX="\n\n>>>>>>>> "

.PHONY: test
test: clean
	@echo -e $(GR)$(PREFIX)prepare tests..$(NC)
	mkdir -p $(CUR) $(IPC)
	@echo -e $(GR)$(PREFIX)test docs..$(NC)
	$(NSA) -h > $(CUR)/-h
	$(NSA) -v > $(CUR)/-v
	$(DIFF)     $(TRU)/-h $(CUR)/-h
	$(DIFF)     $(TRU)/-v $(CUR)/-v
	@echo -e $(GR)$(PREFIX)test create..$(NC)
	$(PASS2) | $(NSA_CREATE)
	$(PASS) | $(DEC) > $(CUR)/$(DB).create.str
	$(CLN) $(CUR)/$(DB).create.str > $(CUR)/$(DB).create.str.cln
	$(DIFF) $(TRU)/$(DB).create.str.cln $(CUR)/$(DB).create.str.cln
	@echo -e $(GR)$(PREFIX)test start..$(NC)
	$(PASS) | $(NSA_START)
	sleep 10
	@echo -e $(GR)$(PREFIX)test ignorable actions..$(NC)
	$(NSA_DIFF)
	$(NSA_DROP)
	$(NSA_COMMIT)
	@echo -e $(GR)$(PREFIX)test add without a commit..$(NC)
	$(NSA_ADD) -t tag1 tag2 -n "oy vey" -f $(TRU)/data
	$(NSA_ADD) -t test asd dea s
	$(NSA_ADD) -t test
	$(PASS_USR) | $(NSA_ADD) -t asdfa lel -m
	$(PASS) | $(DEC) > $(CUR)/$(DB).add_wo_commit.str
	$(CLN) $(CUR)/$(DB).add_wo_commit.str > $(CUR)/$(DB).add_wo_commit.str.cln
	$(DIFF) $(TRU)/$(DB).add_wo_commit.str.cln $(CUR)/$(DB).add_wo_commit.str.cln
	@echo -e $(GR)$(PREFIX)test restart midways..$(NC)
	$(NSA_STOP)
	$(PASS) | $(NSA_START)
	sleep 10
	@echo -e $(GR)$(PREFIX)test commit the pending add..$(NC)
	$(NSA_COMMIT)
	$(PASS) | $(DEC) > $(CUR)/$(DB).add.str
	$(CLN) $(CUR)/$(DB).add.str > $(CUR)/$(DB).add.str.cln
	$(DIFF) $(TRU)/$(DB).add.str.cln $(CUR)/$(DB).add.str.cln
	@echo -e $(GR)$(PREFIX)test del without a commit..$(NC)
	$(NSA_DEL) test
	$(PASS) | $(DEC) > $(CUR)/$(DB).del_wo_commit.str
	$(CLN) $(CUR)/$(DB).del_wo_commit.str > $(CUR)/$(DB).del_wo_commit.str.cln
	$(DIFF) $(TRU)/$(DB).del_wo_commit.str.cln $(CUR)/$(DB).del_wo_commit.str.cln
	@echo -e $(GR)$(PREFIX)test restart midways..$(NC)
	$(NSA_STOP)
	$(PASS) | $(NSA_START)
	sleep 10
	@echo -e $(GR)$(PREFIX)test commit the pending del..$(NC)
	$(NSA_COMMIT)
	$(PASS) | $(DEC) > $(CUR)/$(DB).del.str
	$(CLN) $(CUR)/$(DB).del.str > $(CUR)/$(DB).del.str.cln
	$(DIFF) $(TRU)/$(DB).del.str.cln $(CUR)/$(DB).del.str.cln
	@echo -e $(GR)$(PREFIX)test mod without a commit..$(NC)
	$(NSA_MOD) t t -u barak -r https://mossad.gov.il
	$(NSA_MOD) t d -f $(TRU)/data
	$(PASS_USR) | $(NSA_MOD) t t -m
	$(PASS) | $(DEC) > $(CUR)/$(DB).mod_wo_commit.str
	$(CLN) $(CUR)/$(DB).mod_wo_commit.str > $(CUR)/$(DB).mod_wo_commit.str.cln
	$(DIFF) $(TRU)/$(DB).mod_wo_commit.str.cln $(CUR)/$(DB).mod_wo_commit.str.cln
	@echo -e $(GR)$(PREFIX)test restart midways..$(NC)
	$(NSA_STOP)
	$(PASS) | $(NSA_START)
	sleep 10
	@echo -e $(GR)$(PREFIX)test commit the pending mod..$(NC)
	$(NSA_COMMIT)
	$(PASS) | $(DEC) > $(CUR)/$(DB).mod.str
	$(CLN) $(CUR)/$(DB).mod.str > $(CUR)/$(DB).mod.str.cln
	$(DIFF) $(TRU)/$(DB).mod.str.cln $(CUR)/$(DB).mod.str.cln
	@echo -e $(GR)$(PREFIX)test do..$(NC)
	$(NSA_DO) t t -c cat > $(CUR)/data-t_t
	$(NSA_DO) t d -c cat > $(CUR)/data-t_d
	$(DIFF) $(TRU)/data $(CUR)/data-t_t
	$(DIFF) $(TRU)/data $(CUR)/data-t_d
	@echo -e $(GR)$(PREFIX)test ls..$(NC)
	$(NSA_LS)
	@echo -e $(GR)$(PREFIX)test chpass..$(NC)
	$(PASS_NEW2) | $(NSA_CHPASS)
	$(NSA_COMMIT)
	$(NSA_STOP)
	$(PASS_NEW) | $(NSA_START)
	sleep 5
	@echo -e $(GR)$(PREFIX)test stop..$(NC)
	$(NSA_STOP)

.PHONY: clean
clean:
	# clean
	rm -rf $(CUR) $(IPC)
