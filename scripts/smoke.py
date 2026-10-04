from pathlib import Path
import json,re,subprocess,time
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
accounts={i:create_account(account_private_key=env('ACCOUNT_'+str(i)+'_GENLAYER_PRIVATE_KEY')) for i in (2,3,4)};clients={i:create_client(chain=studionet,account=a) for i,a in accounts.items()};address=json.loads((R/'deployment.json').read_text())['contractAddress'];sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();stamp=str(int(time.time()));registry='OPS-'+stamp;first='RECOVERY-'+stamp;alias='RESTORE-'+stamp;raw='https://raw.githubusercontent.com/liwaw008-svg/lexicon-turnstile/'+sha+'/evidence/';cdn='https://cdn.jsdelivr.net/gh/liwaw008-svg/lexicon-turnstile@'+sha+'/evidence/';third='https://raw.githack.com/liwaw008-svg/lexicon-turnstile/'+sha+'/evidence/'
def send(who,method,args):
 tx=clients[who].write_contract(address=address,function_name=method,args=args);clients[who].wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000);full=clients[who].get_transaction(transaction_hash=tx);leader=(full.get('consensus_data',{}).get('leader_receipt')or[{}])[0];assert full.get('result_name')=='MAJORITY_AGREE' and leader.get('execution_result')=='SUCCESS',full;return str(tx)
txs={};txs['registry']=send(4,'open_registry',[registry,accounts[3].address,'Community operations vocabulary',raw+'charter.md',900]);txs['first_proposal']=send(2,'propose_term',[registry,first,'Recovery window',cdn+'recovery-window.md']);txs['first_review']=send(3,'review_term',[first]);canonical=clients[4].read_contract(address=address,function_name='get_term',args=[first]);assert canonical['state']=='CANONICAL' and canonical['relation']=='UNIQUE',canonical;txs['alias_proposal']=send(2,'propose_term',[registry,alias,'Restoration interval',third+'restoration-interval.md']);txs['alias_review']=send(3,'review_term',[alias]);state=clients[4].read_contract(address=address,function_name='get_term',args=[alias]);assert state['state']=='ALIAS' and state['matched_term_id']==first,state;out={'registryId':registry,'canonicalTermId':first,'aliasTermId':alias,'transactions':txs,'state':state,'walletDisclosure':'All demo wallets and source fixtures are operator-controlled.'};(R/'network-run.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
