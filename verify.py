"""Data integrity and spherical/ecliptic coordinate regression checks."""
import json,math,gzip
from pathlib import Path
p=Path(__file__).resolve().parent
a=json.loads((p/'stars.json').read_text()); s=a['stars']
assert len(s)==100 and len({x['id'] for x in s})==100
assert s[0]['name']=='Sole' and s[0]['position']==[0,0,0]
assert all(x['kind'].rstrip('?') in ['*','LM','WD'] for x in s)
assert [x['distancePc'] for x in s]==sorted(x['distancePc'] for x in s)
raw=gzip.decompress((p/'tablea1.dat.gz').read_bytes()).decode().splitlines()
expected=sorted([r for r in raw if r[40:46].strip().rstrip('?') in ['*','LM','WD']],key=lambda r:(1000/float(r[114:122]),int(r[:4])))[:99]
assert [r[:4].strip() for r in expected]==[x['id'] for x in s[1:]]
eps=math.radians(23.439291111)
for x in s[1:]:
 assert math.isclose(x['distancePc'],1000/x['parallax'],rel_tol=1e-12)
 xx,zz,minusyy=x['position']; yy=-minusyy
 y=yy*math.cos(eps)-zz*math.sin(eps); z=yy*math.sin(eps)+zz*math.cos(eps)
 recovered_ra=math.degrees(math.atan2(y,xx))%360
 recovered_dec=math.degrees(math.asin(z/x['distanceLy']))
 assert math.isclose(recovered_ra,x['ra'],abs_tol=1e-8)
 assert math.isclose(recovered_dec,x['dec'],abs_tol=1e-8)
 assert math.isclose(math.sqrt(sum(v*v for v in x['position'])),x['distanceLy'],rel_tol=1e-12)
assert s[1]['name']=='Proxima Centauri' and 4.24<s[1]['distanceLy']<4.26
assert s[-1]['name']=='36 Oph B' and a['meta']['nextExcluded']['distanceLy']>s[-1]['distanceLy']
assert any(x['kind']=='LM?' for x in s)
assert any(x['kind']=='WD' for x in s)
print('PASS: 100 unique entries, exact catalogue selection, ranking/cutoff, parsec conversion, inverse ecliptic transform, uncertain types and white dwarfs.')
