"""Rebuild 100 entries from the archived CDS catalogue (2023-08-25). No invented measurements."""
import gzip,json,math,hashlib,sys
from pathlib import Path
root=Path(__file__).resolve().parent
raw=gzip.decompress((root/'tablea1.dat.gz').read_bytes())
def num(s):
 try:return float(s.strip())
 except ValueError:return None
aliases={'Wolf 359':'Wolf 359','Ross 128':'Ross 128','Ross 248':'Ross 248','Proxima Cen':'Proxima Centauri','alf Cen A':'Alpha Centauri A','alf Cen B':'Alpha Centauri B','alf CMa A':'Sirius A','alf CMa B':'Sirius B','alf CMi A':'Procyon A','alf CMi B':'Procyon B','eps Eri':'Epsilon Eridani','eps Ind A':'Epsilon Indi A','tau Cet':'Tau Ceti','alf Aql':'Altair','GJ 866 A':'EZ Aquarii A','GJ 866 B':'EZ Aquarii B','GJ 866 C':'EZ Aquarii C','GJ 166 A':'40 Eridani A','GJ 166 B':'40 Eridani B','GJ 166 C':'40 Eridani C','sig Dra':'Sigma Draconis','eta Cas A':'Eta Cassiopeiae A','eta Cas B':'Eta Cassiopeiae B'}
major={'Proxima Centauri','Alpha Centauri A',"Barnard's Star",'Wolf 359','Lalande 21185','Sirius A','Ross 154','Ross 128','Epsilon Eridani','Tau Ceti','Procyon A','Epsilon Indi A',"Luyten's Star",'Altair','61 Cyg A','40 Eridani A',"Teegarden's Star",'Wolf 1061'}
rows=[]
for r in raw.decode().splitlines():
 kind=r[40:46].strip()
 if kind.rstrip('?') not in ['*','LM','WD']:continue
 name=r[47:76].strip(); common=r[544:561].strip(); ra=num(r[78:91]); dec=num(r[93:106]); plx=num(r[114:122]); d=1000/plx; ly=d*3.261563777
 a=math.radians(ra); b=math.radians(dec); eps=math.radians(23.439291111)
 x=ly*math.cos(b)*math.cos(a); y=ly*math.cos(b)*math.sin(a); z=ly*math.sin(b)
 display=aliases.get(name,common or name)
 rows.append(dict(id=r[:4].strip(),system=r[5:9].strip(),name=display,catalogName=name,commonName=common,kind=kind,spectral=r[301:309].strip() or None,ra=ra,dec=dec,epoch=num(r[107:113]),parallax=plx,parallaxError=num(r[123:131]),parallaxRef=r[132:163].strip(),distancePc=d,distanceLy=ly,position=[x,z*math.cos(eps)-y*math.sin(eps),-(y*math.cos(eps)+z*math.sin(eps))],g=num(r[352:361]),gEstimated=num(r[362:368]),v=num(r[405:412]),bp=num(r[369:378]),rp=num(r[379:388]),pmRa=num(r[164:180]),pmDec=num(r[198:214]),rv=num(r[263:271]),gaiaId=r[497:516].strip().replace('---','') or None,major=display in major))
rows.sort(key=lambda r:(r['distancePc'],int(r['id'])))
sun=dict(id='sun',system='sun',name='Sole',catalogName='Sun',kind='*',spectral='G2 V',ra=None,dec=None,epoch=None,parallax=None,parallaxError=None,parallaxRef=None,distancePc=0,distanceLy=0,position=[0,0,0],g=None,gEstimated=None,v=None,bp=None,rp=None,pmRa=None,pmDec=None,rv=None,gaiaId=None,major=True)
selected=[sun]+rows[:99]
for i,r in enumerate(selected):r['rank']=i+1
out={'meta':{'title':'The 10 parsec sample in the Gaia era','catalogue':'CDS J/A+A/650/A201','version':'2023-08-25','retrieved':'2026-10-03','source':'https://cdsarc.cds.unistra.fr/ftp/J/A+A/650/A201/','doi':'https://doi.org/10.1051/0004-6361/202140985','update':'https://arxiv.org/abs/2302.02810','sha256':hashlib.sha256(raw).hexdigest(),'selection':'99 entries of type *, LM, LM?, WD or WD? ordered by 1000/parallax, plus the Sun. Brown dwarfs and planets excluded. Question marks retained. Component stars counted separately.','frame':'Equatorial ICRS positions at each catalogue epoch, rotated to mean J2000 ecliptic axes using obliquity 23.439291111 deg. No epoch propagation or orbital simulation. Distances = 1000/parallax mas. Renderer axes: (ecliptic X, ecliptic Z, -ecliptic Y).','maxLy':selected[-1]['distanceLy'],'nextExcluded':{'name':rows[99]['name'],'distanceLy':rows[99]['distanceLy']}},'stars':selected}
if '--check' in sys.argv:
 snapshot=json.loads((root/'stars.json').read_text())
 assert len(snapshot['stars'])==len(out['stars']), 'Catalogue size changed'
 for saved,generated in zip(snapshot['stars'],out['stars']):
  assert len(saved['position'])==3
  assert all(math.isclose(a,b,rel_tol=0,abs_tol=1e-12) for a,b in zip(saved['position'],generated['position'])), 'Position changed beyond floating-point tolerance'
  # libm implementations differ at their final bits; all other data must match exactly.
  generated['position']=saved['position']
 assert snapshot==out, 'Catalogue metadata or measurements changed'
 print('Reproducibility check passed (position tolerance 1e-12 light-years)')
else:
 (root/'stars.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
assert len(selected)==100 and len({r['id'] for r in selected})==100
for r in selected: assert abs(math.sqrt(sum(v*v for v in r['position']))-r['distanceLy'])<1e-10
print('100 entries; boundary:',selected[-1]['name'],round(selected[-1]['distanceLy'],3),'ly; next:',rows[99]['name'])
