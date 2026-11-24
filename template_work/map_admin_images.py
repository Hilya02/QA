from docx import Document
from pathlib import Path
from zipfile import ZipFile
from PIL import Image
import io
p=Path(r'C:\Users\HilyaNtinda\Downloads\Admin user dashboard updated.docx')
d=Document(p)
print('PARAGRAPH IMAGE MAP')
for i,para in enumerate(d.paragraphs):
    refs=[]
    for r in para.runs:
        for blip in r._element.iter():
            if blip.tag.endswith('}blip'):
                rid=blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                if rid:
                    rel=para.part.related_parts.get(rid)
                    refs.append((rid,getattr(rel,'partname',None),getattr(rel,'blob',b'') and len(rel.blob)))
    if para.text.strip() or refs: print(i,'TEXT=',repr(para.text),'IMAGES=',refs)
print('MEDIA INVENTORY')
with ZipFile(p) as z:
    for name in z.namelist():
        if name.startswith('word/media/'):
            b=z.read(name)
            try:
                im=Image.open(io.BytesIO(b)); print(name,len(b),im.format,im.size)
            except Exception: print(name,len(b),'unknown')
