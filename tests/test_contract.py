from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
def test_public_surface():
 for name in ('open_registry','propose_term','review_term','revise_conflict','expire_term','close_registry','get_registry','get_term'):assert 'def '+name in S
def test_consensus_recomputes_every_field():assert "run()==leader.calldata" in S and "matched_digest" in S
def test_relation_match_cannot_diverge():assert "relation=='UNIQUE' and index!=-1" in S and "index>=len(existing)" in S
def test_sources_and_recovery():assert "origin==r.charter_origin" in S and "origin!=t.definition_origin" in S and "now()<=int(t.deadline)" in S
def test_unique_ids_and_bounded_registry():assert "key in self.terms" in S and "len(ids)>=8" in S
