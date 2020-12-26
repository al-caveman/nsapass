NSA=../nsa -s -d $(CUR)/db.ciphart
CPH=ciphart
TRU=./truth
CUR=./current
PAS=echo -e "lol\nlol"
NEWPAS=echo -e "rofl\nlol"
CHN1PAS=echo -e "lol\nlmfao"
CHN2PAS=echo -e "lmfao\nlol"
STR=python ./striptimestamps.py
DIF=diff --color=always -u

.PHONY: test
test: test-docs test-chpass test-cat test-forget-archived

.PHONY: test-prepare
test-prepare:
	make clean
	mkdir -p $(CUR)

.PHONY: test-docs
test-docs: test-prepare
	$(NSA) -h > $(CUR)/-h
	$(NSA) -v > $(CUR)/-v
	$(DIF) 	    $(CUR)/-h $(TRU)/-h
	$(DIF) 	    $(CUR)/-v $(TRU)/-v

.PHONY: test-add
test-add: test-prepare
	$(PAS) | $(NSA) add tag1 tag2 -m -n "test note"
	$(PAS) | $(NSA) add tag3 -m
	$(PAS) | $(NSA) add tag4 -f $(TRU)/data1.clr
	$(PAS) | $(CPH) -dks -i $(CUR)/db.ciphart -o $(CUR)/db.json
	$(STR) $(CUR)/db.json > $(CUR)/db_stripped.json
	$(DIF) $(CUR)/db_stripped.json $(TRU)/db_add_stripped.json

.PHONY: test-cat
test-cat: test-add
	$(PAS) | $(NSA) -s cat tag4 > $(CUR)/data1.clr
	$(DIF) $(CUR)/data1.clr $(TRU)/data1.clr

.PHONY: test-del
test-del: test-add
	$(PAS) | $(NSA) del tag1 tag2
	$(PAS) | $(NSA) del tag3
	$(PAS) | $(NSA) del tag4
	$(PAS) | $(CPH) -dks -i $(CUR)/db.ciphart -o $(CUR)/db.json
	$(STR) $(CUR)/db.json > $(CUR)/db_stripped.json
	$(DIF) $(CUR)/db_stripped.json $(TRU)/db_del_stripped.json

.PHONY: test-undel
test-undel: test-del
	$(PAS) | $(NSA) undel tag1 tag2
	$(PAS) | $(NSA) undel tag3
	$(PAS) | $(NSA) undel tag4
	$(PAS) | $(CPH) -dks -i $(CUR)/db.ciphart -o $(CUR)/db.json
	$(STR) $(CUR)/db.json > $(CUR)/db_stripped.json
	$(DIF) $(CUR)/db_stripped.json $(TRU)/db_undel_stripped.json

.PHONY: test-mod
test-mod: test-undel
	$(NEWPAS) | $(NSA) mod tag1 tag2 -t tagNEW1 -m -n "new pass"
	$(PAS) | $(NSA) mod tag3 -u usernamelol
	$(PAS) | $(NSA) mod tag4 -f $(TRU)/data2.clr -n "file updated!"
	$(PAS) | $(NSA) -s cat tag4 > $(CUR)/data2.clr
	$(PAS) | $(CPH) -dks -i $(CUR)/db.ciphart -o $(CUR)/db.json
	$(STR) $(CUR)/db.json > $(CUR)/db_stripped.json
	$(DIF) $(CUR)/db_stripped.json $(TRU)/db_mod_stripped.json
	$(DIF) $(CUR)/data2.clr $(TRU)/data2.clr

.PHONY: test-undo
test-undo: test-mod
	$(PAS) | $(NSA) undo tagNEW1 -r 1
	$(PAS) | $(NSA) undo tag3 -r 2
	$(PAS) | $(NSA) undo tag4 -r 3
	$(PAS) | $(CPH) -dks -i $(CUR)/db.ciphart -o $(CUR)/db.json
	$(STR) $(CUR)/db.json > $(CUR)/db_stripped.json
	$(DIF) $(CUR)/db_stripped.json $(TRU)/db_undo_stripped.json

.PHONY: test-forget
test-forget: test-undo
	$(PAS) | $(NSA) forget -r 0
	$(PAS) | $(CPH) -dks -i $(CUR)/db.ciphart -o $(CUR)/db.json
	$(STR) $(CUR)/db.json > $(CUR)/db_stripped.json
	$(DIF) $(CUR)/db_stripped.json $(TRU)/db_forget_stripped.json

.PHONY: test-forget-archived
test-forget-archived: test-forget
	$(PAS) | $(NSA) forget -a -r 0
	$(PAS) | $(CPH) -dks -i $(CUR)/db.ciphart -o $(CUR)/db.json
	$(STR) $(CUR)/db.json > $(CUR)/db_stripped.json
	$(DIF) $(CUR)/db_stripped.json $(TRU)/db_forget-archived_stripped.json

.PHONY: test-chpass
test-chpass: test-prepare test-add
	$(CHN1PAS) | $(NSA) chpass
	$(CHN2PAS) | $(NSA) chpass

.PHONY: clean
clean:
	rm -rf $(CUR)
