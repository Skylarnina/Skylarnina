const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
/* Kóda: build self-contained HTML frames for Figma's html_to_figma importer.
   Usage: NODE_PATH=$(npm root -g) node koda/tools/figma-build.js   (needs Playwright + Chromium, PIL for image resize)
   Output: koda/exports/figma/koda-*.html, one <div id="frame"> per file (desktop 1440, mobile 390, booking overlay states, wireframes).
   Fonts: five TTFs in FONTDIR (f1 Cormorant Garamond Italic, f2 Light, f3 Regular, f4 Inter Light, f5 Inter Medium) are inlined as @font-face. */
const FONTDIR=process.env.KODA_FONTS||process.env.HOME+'/.local/share/fonts/koda';
const SITE=path.resolve(__dirname,'../site/v3'), OUT=path.resolve(__dirname,'../exports/figma'), IMG=path.join(OUT,'img'); fs.mkdirSync(IMG,{recursive:true});
const FONTS=[['f1','Cormorant Garamond','italic',400],['f2','Cormorant Garamond','normal',300],['f3','Cormorant Garamond','normal',400],['f4','Inter','normal',300],['f5','Inter','normal',500]];
const fontCss=FONTS.map(([f,fam,sty,w])=>`@font-face{font-family:'${fam}';font-style:${sty};font-weight:${w};src:url(data:font/ttf;base64,${fs.readFileSync(path.join(FONTDIR,f+'.ttf')).toString('base64')}) format('truetype');}`).join('\n');
const dataUri=n=>'data:image/jpeg;base64,'+fs.readFileSync(path.join(IMG,n)).toString('base64');
const VARIANTS=[
 {name:'desktop',   src:'index.html',     W:1440,H:900, mobile:false},
 {name:'mobile',    src:'index.html',     W:390, H:844, mobile:true},
 {name:'booking-desktop',src:'index.html',W:1440,H:900, mobile:false, booking:'night'},
 {name:'booking-mobile', src:'index.html',W:390, H:844, mobile:true,  booking:'night'},
 {name:'wireframe-desktop',src:'wireframe.html',W:1440,H:900,mobile:false, wire:true},
 {name:'wireframe-mobile', src:'wireframe.html',W:390, H:844,mobile:true,  wire:true},
];
(async()=>{
 if(!fs.readdirSync(IMG).length){ require('child_process').execSync(`python3 - <<'PY'
from PIL import Image, ImageOps
import os, glob
src=${JSON.stringify(path.resolve(__dirname,'../site/v2/media/colour'))}; out=${JSON.stringify(IMG)}
for f in sorted(glob.glob(src+'/*.jpg')):
    im=ImageOps.exif_transpose(Image.open(f)).convert('RGB'); w,h=im.size
    if w>2000: im=im.resize((2000, round(h*2000/w)), Image.LANCZOS)
    im.save(os.path.join(out,os.path.basename(f)),'JPEG',quality=82,optimize=True)
PY`,{stdio:'inherit'}); }
 const b=await chromium.launch();
 for(const v of VARIANTS){
  const wrap=path.join(SITE,'_fig_'+v.name+'.html');
  fs.writeFileSync(wrap,'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'+fs.readFileSync(path.join(SITE,v.src),'utf8')+'</body></html>');
  const ctx=await b.newContext({viewport:{width:v.W,height:v.H}});
  await ctx.addInitScript(()=>{try{localStorage.setItem('koda-motion','enhanced');localStorage.setItem('koda-look','colour');}catch(e){}});
  const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('file://'+wrap); await p.waitForTimeout(1500);
  if(!v.wire) await p.waitForFunction(()=>[...document.querySelectorAll('.ph[data-src]')].every(e=>e.classList.contains('has-media')),null,{timeout:15000}).catch(()=>console.log(v.name,'some media not loaded'));
  if(v.booking){ await p.click('#book-'+v.booking); await p.waitForTimeout(600); }
  // image map
  const imgs={}; for(const n of fs.readdirSync(IMG)) imgs[n]=dataUri(n);
  const html=await p.evaluate(({imgs,v})=>{
    const $$=s=>Array.from(document.querySelectorAll(s));
    $$('script,link,video,.proto,#sticky').forEach(e=>e.remove());
    $$('.will-fade,.fade').forEach(e=>{e.classList.remove('will-fade','fade');});
    $$('.ph[data-src]').forEach(ph=>{ const n=ph.dataset.src.split('/').pop(); if(v.wire){ ph.style.backgroundImage=''; return; } if(imgs[n]){ ph.style.backgroundImage='url("'+imgs[n]+'")'; if(ph.dataset.pos) ph.style.backgroundPosition=ph.dataset.pos; ph.classList.add('has-media'); } });
    const bk=document.getElementById('booking');
    if(v.booking){ bk.hidden=false; bk.classList.add('is-open'); bk.style.cssText='position:absolute;top:0;left:0;width:'+v.W+'px;height:'+v.H+'px;opacity:1;overflow:hidden;';
      document.body.style.cssText='height:'+v.H+'px;overflow:hidden;position:relative;'; document.documentElement.style.cssText='height:'+v.H+'px;overflow:hidden;'; }
    else if(bk) bk.remove();
    // pin scroll position 0 for the frozen doc
    document.body.removeAttribute('class');
    const fr=document.createElement('div'); fr.id='frame'; fr.style.cssText='position:relative;width:'+v.W+'px;overflow:hidden;background:#FAFAF8;'+(v.booking?'height:'+v.H+'px;':'');
    while(document.body.firstChild) fr.appendChild(document.body.firstChild); document.body.appendChild(fr);
    return document.documentElement.outerHTML;
  },{imgs,v});
  await ctx.close(); fs.unlinkSync(wrap);
  // CSS rewrite: viewport units -> px, media queries -> unconditional/none, fixed -> absolute
  const W=v.W,H=v.H;
  let out=html.replace(/<style([^>]*)>([\s\S]*?)<\/style>/g,(m,attrs,css)=>{
    css=css.replace(/(\d*\.?\d+)(s|d)?vh\b/g,(_,n)=>(+n*H/100).toFixed(2)+'px').replace(/(\d*\.?\d+)(s|d)?vw\b/g,(_,n)=>(+n*W/100).toFixed(2)+'px');
    css=css.replace(/@media\s*\(max-width:\s*899px\)/g,v.mobile?'@media all':'@media not all')
           .replace(/@media\s*\(min-width:\s*900px\)/g,v.mobile?'@media not all':'@media all')
           .replace(/@media\s*\(max-width:\s*1100px\)\s*and\s*\(min-width:\s*900px\)/g,'@media not all')
           .replace(/@media\s*\(prefers-reduced-motion:\s*reduce\)/g,'@media not all')
           .replace(/position:\s*fixed/g,'position:absolute')
           .replace(/env\(safe-area-inset-[a-z]+,\s*0px\)/g,'0px');
    return '<style'+attrs+'>'+css+'</style>';
  });
  const head='<meta charset="utf-8"><meta name="viewport" content="width='+W+'"><title>Kóda · '+v.name+'</title><style>'+fontCss+'\nhtml,body{width:'+W+'px;min-width:'+W+'px;max-width:'+W+'px;margin:0;overflow-x:hidden}*,*::before,*::after{transition:none!important;animation:none!important}.will-fade{opacity:1!important}</style>';
  out=out.replace(/<head>/,'<head>'+head);
  out='<!doctype html>'+out.replace(/^<html/,'<html');
  const f=path.join(OUT,'koda-'+v.name+'.html'); fs.writeFileSync(f,out);
  console.log(v.name,(fs.statSync(f).size/1048576).toFixed(1)+'MB','errors:',errs.length?errs:'none');
 }
 await b.close();
})();
