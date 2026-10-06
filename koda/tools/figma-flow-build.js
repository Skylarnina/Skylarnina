/* Builds a self-contained copy of koda/site/v4/flow.html for Figma's html_to_figma importer.
   Post it with cssSelector ".cell > .scr, .desk": each screen and the desktop card become their own frame. */
const fs=require('fs'),path=require('path');
const FONTDIR=process.env.KODA_FONTS||process.env.HOME+'/.local/share/fonts/koda';
const FONTS=[['f1','Cormorant Garamond','italic',400],['f2','Cormorant Garamond','normal',300],['f3','Cormorant Garamond','normal',400],['f4','Inter','normal',300],['f5','Inter','normal',500]];
const fontCss=FONTS.map(([f,fam,sty,w])=>`@font-face{font-family:'${fam}';font-style:${sty};font-weight:${w};src:url(data:font/ttf;base64,${fs.readFileSync(path.join(FONTDIR,f+'.ttf')).toString('base64')}) format('truetype');}`).join('\n');
let src=fs.readFileSync(path.resolve(__dirname,'../site/v4/flow.html'),'utf8').replace(/<link[^>]*>\s*/g,'').replace(/<script>[\s\S]*?<\/script>/g,'');
const i=src.indexOf('<div class="board"'); const head=src.slice(0,i), body=src.slice(i);
const out=path.resolve(__dirname,'../exports/figma/v4/koda-flow.html'); fs.mkdirSync(path.dirname(out),{recursive:true});
fs.writeFileSync(out,'<!doctype html><html lang="en" data-motion="enhanced"><head><meta charset="utf-8"><meta name="viewport" content="width=1800"><style>'+fontCss+'\nhtml,body{width:1800px;margin:0}</style>'+head+'</head><body>'+body+'</body></html>');
console.log('wrote',out,(fs.statSync(out).size/1048576).toFixed(1)+'MB');
