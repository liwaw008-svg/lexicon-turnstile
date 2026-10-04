from pathlib import Path
import json,re
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as ca
R=Path(__file__).parents[1];ROOT=R.parents[3]
def env(name):
 text=(ROOT/'accounts.env').read_text();return re.search(r'^'+re.escape(name)+r'\s*=\s*"?([^"\r\n]+)',text,re.M).group(1).strip()
def calldata(method=None,args=None,kwargs=None):
 out={}
 if method is not None:out['method']=method
 if args:out['args']=args
 if kwargs:out['kwargs']=kwargs
 return out
ca.make_calldata_object=calldata
client=create_client(chain=studionet,account=create_account(account_private_key=env('ACCOUNT_2_GENLAYER_PRIVATE_KEY')));address=json.loads((R/'deployment.json').read_text())['contractAddress'];run=json.loads((R/'network-run.json').read_text());term=run['canonicalTermId'];tx=client.write_contract(address=address,function_name='review_term',args=[term]);client.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000);full=client.get_transaction(transaction_hash=tx);leader=(full.get('consensus_data',{}).get('leader_receipt')or[{}])[0];result=leader.get('result');message=str(result.get('payload','') if isinstance(result,dict) else result)
assert leader.get('execution_result')=='ERROR' and '[EXPECTED]' in message,full
out={'guard':'replay or unauthorized review is rejected','transaction':str(tx),'consensus':full.get('result_name'),'execution':leader.get('execution_result'),'expectedMarker':'[EXPECTED]'};(R/'negative-run.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
