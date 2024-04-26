import{A as F,a as j,r as x}from"./router.95851ad5.js";import{_ as U}from"./DocsButton.vue_vue_type_script_setup_true_lang.47e2aae4.js";import{i as O}from"./url.20f0444a.js";import{d as E,Z as S,J as T,b as n,ew as v,dj as M,ey as h,eB as G,e as _,I as R,r as z,c as r,w as l,u as s,f as c,as as y,eH as f,eF as D,bz as q,af as J,aE as I,cB as L,a as W,bG as Y,cE as Q,ex as X,bE as K,bi as ee,bg as te,eG as ae,cy as le,bh as ne,cC as se,x as oe}from"./outputWidgets.c7d11ead.js";import{A as P}from"./Paragraph.a2d4bb5b.js";import{A as ue,F as re}from"./Form.894c92e7.js";import{M as ie}from"./Modal.7ab5d69d.js";import{A as H}from"./index.8343729f.js";import{A as pe}from"./Title.fdf5c01d.js";import{A as $}from"./Text.eba38ee8.js";import{A as ce}from"./index.e53fe664.js";(function(){try{var g=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},d=new Error().stack;d&&(g._sentryDebugIds=g._sentryDebugIds||{},g._sentryDebugIds[d]="be5badcf-6033-41dd-95b1-fc3c03d70437",g._sentryDebugIdIdentifier="sentry-dbid-be5badcf-6033-41dd-95b1-fc3c03d70437")}catch{}})();const de=["width","height","fill","transform"],ye={key:0},me=_("path",{d:"M144,128a16,16,0,1,1-16-16A16,16,0,0,1,144,128ZM60,112a16,16,0,1,0,16,16A16,16,0,0,0,60,112Zm136,0a16,16,0,1,0,16,16A16,16,0,0,0,196,112Z"},null,-1),fe=[me],ve={key:1},ge=_("path",{d:"M240,96v64a16,16,0,0,1-16,16H32a16,16,0,0,1-16-16V96A16,16,0,0,1,32,80H224A16,16,0,0,1,240,96Z",opacity:"0.2"},null,-1),he=_("path",{d:"M140,128a12,12,0,1,1-12-12A12,12,0,0,1,140,128Zm56-12a12,12,0,1,0,12,12A12,12,0,0,0,196,116ZM60,116a12,12,0,1,0,12,12A12,12,0,0,0,60,116Z"},null,-1),Ae=[ge,he],be={key:2},ke=_("path",{d:"M224,80H32A16,16,0,0,0,16,96v64a16,16,0,0,0,16,16H224a16,16,0,0,0,16-16V96A16,16,0,0,0,224,80ZM60,140a12,12,0,1,1,12-12A12,12,0,0,1,60,140Zm68,0a12,12,0,1,1,12-12A12,12,0,0,1,128,140Zm68,0a12,12,0,1,1,12-12A12,12,0,0,1,196,140Z"},null,-1),_e=[ke],we={key:3},Ce=_("path",{d:"M138,128a10,10,0,1,1-10-10A10,10,0,0,1,138,128ZM60,118a10,10,0,1,0,10,10A10,10,0,0,0,60,118Zm136,0a10,10,0,1,0,10,10A10,10,0,0,0,196,118Z"},null,-1),Ve=[Ce],Ze={key:4},Me=_("path",{d:"M140,128a12,12,0,1,1-12-12A12,12,0,0,1,140,128Zm56-12a12,12,0,1,0,12,12A12,12,0,0,0,196,116ZM60,116a12,12,0,1,0,12,12A12,12,0,0,0,60,116Z"},null,-1),Be=[Me],Te={key:5},Se=_("path",{d:"M136,128a8,8,0,1,1-8-8A8,8,0,0,1,136,128Zm-76-8a8,8,0,1,0,8,8A8,8,0,0,0,60,120Zm136,0a8,8,0,1,0,8,8A8,8,0,0,0,196,120Z"},null,-1),$e=[Se],Ie={name:"PhDotsThree"},Ne=E({...Ie,props:{weight:{type:String},size:{type:[String,Number]},color:{type:String},mirrored:{type:Boolean}},setup(g){const d=g,w=S("weight","regular"),k=S("size","1em"),B=S("color","currentColor"),u=S("mirrored",!1),m=T(()=>{var p;return(p=d.weight)!=null?p:w}),Z=T(()=>{var p;return(p=d.size)!=null?p:k}),C=T(()=>{var p;return(p=d.color)!=null?p:B}),t=T(()=>d.mirrored!==void 0?d.mirrored?"scale(-1, 1)":void 0:u?"scale(-1, 1)":void 0);return(p,V)=>(n(),v("svg",G({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 256 256",width:Z.value,height:Z.value,fill:C.value,transform:t.value},p.$attrs),[M(p.$slots,"default"),m.value==="bold"?(n(),v("g",ye,fe)):m.value==="duotone"?(n(),v("g",ve,Ae)):m.value==="fill"?(n(),v("g",be,_e)):m.value==="light"?(n(),v("g",we,Ve)):m.value==="regular"?(n(),v("g",Ze,Be)):m.value==="thin"?(n(),v("g",Te,$e)):h("",!0)],16,de))}}),ze=E({__name:"CreationModal",props:{entityName:{},fields:{}},emits:["create"],setup(g,{expose:d,emit:w}){const k=g,B=`Create a new ${k.entityName}`,u=R({inputValue:{}}),m=z(!1),Z=()=>m.value=!0,C=()=>m.value=!1,t=()=>{w("create",u.inputValue),u.inputValue={},C()},p=(A,a)=>{const e=A.target.value,o=k.fields.find(b=>b.key===a);o!=null&&o.format?u.inputValue[a]=o.format(e):u.inputValue[a]=e},V=(A,a)=>{const e=A.target.value,o=k.fields.find(b=>b.key===a);o!=null&&o.blur?u.inputValue[a]=o.blur(e):u.inputValue[a]=e};return d({open:Z,close:C}),(A,a)=>(n(),r(s(ie),{open:m.value,title:B,onCancel:C,onOk:t},{default:l(()=>[c(s(P),null,{default:l(()=>[y(" You may edit the "+f(A.entityName)+" name afterwards at Settings. ",1)]),_:1}),c(s(re),{layout:"vertical"},{default:l(()=>[(n(!0),v(I,null,D(A.fields,e=>{var o;return n(),r(s(ue),{key:e.key,label:e.label,help:(o=e.hint)==null?void 0:o.call(e,u.inputValue[e.key])},{default:l(()=>{var b,N;return[!e.type||typeof e.type=="string"?(n(),r(s(q),{key:0,value:u.inputValue[e.key],"onUpdate:value":i=>u.inputValue[e.key]=i,placeholder:(b=e.placeholder)!=null?b:"",type:(N=e.type)!=null?N:"text",onInput:i=>p(i,e.key),onBlur:i=>V(i,e.key)},null,8,["value","onUpdate:value","placeholder","type","onInput","onBlur"])):Array.isArray(e.type)?(n(),r(s(J),{key:1,value:u.inputValue[e.key],"onUpdate:value":i=>u.inputValue[e.key]=i},{default:l(()=>[(n(!0),v(I,null,D(e.type,i=>(n(),r(s(L),{key:typeof i=="string"?i:i.value,value:typeof i=="string"?i:i.value},{default:l(()=>[y(f(typeof i=="string"?i:i.label),1)]),_:2},1032,["value"]))),128))]),_:2},1032,["value","onUpdate:value"])):h("",!0)]}),_:2},1032,["label","help"])}),128))]),_:1})]),_:1},8,["open"]))}}),De={class:"action-item"},Pe=E({__name:"CrudView",props:{table:{},loading:{type:Boolean},title:{},emptyTitle:{},entityName:{},description:{},createButtonText:{},docsPath:{},live:{type:Boolean},fields:{}},emits:["create"],setup(g,{emit:d}){const w=g,k=z(null),B=()=>{var t;w.fields?(t=k.value)==null||t.open():d("create",{})},u=z(!1);async function m(t,p){var V;if(!u.value){u.value=!0;try{"onClick"in t?await((V=t.onClick)==null?void 0:V.call(t,{key:p.key})):"link"in t&&(typeof t.link=="string"&&O(t.link)?open(t.link,"_blank"):x.push(t.link))}finally{u.value=!1}}}async function Z(t){d("create",t)}const C=T(()=>({"--columnCount":`${w.table.columns.length}`}));return(t,p)=>{const V=W("router-link");return n(),v(I,null,[c(s(se),{direction:"vertical",class:"crud-view"},{default:l(()=>{var A;return[c(s(H),{align:"center",justify:"space-between"},{default:l(()=>[t.title?(n(),r(s(pe),{key:0},{default:l(()=>[y(f(t.title),1)]),_:1})):h("",!0),M(t.$slots,"more",{},void 0,!0)]),_:3}),t.description?(n(),r(s(P),{key:0},{default:l(()=>[y(f(t.description)+" ",1),M(t.$slots,"description",{},void 0,!0),t.docsPath?(n(),r(U,{key:0,path:t.docsPath},null,8,["path"])):h("",!0)]),_:3})):h("",!0),c(s(H),{gap:"middle"},{default:l(()=>[t.createButtonText?(n(),r(s(Y),{key:0,type:"primary",onClick:B},{default:l(()=>[y(f(t.createButtonText),1)]),_:1})):h("",!0),M(t.$slots,"secondary",{},void 0,!0)]),_:3}),M(t.$slots,"extra",{},void 0,!0),c(s(Q),{size:"small",style:X(C.value),"data-source":t.table.rows,loading:u.value||t.loading&&!t.live,height:400,columns:(A=t.table.columns)==null?void 0:A.map(({name:a,align:e},o,b)=>({title:a,key:o,align:e!=null?e:"center"}))},{emptyText:l(()=>[y(f(t.emptyTitle),1)]),headerCell:l(a=>[y(f(a.title),1)]),bodyCell:l(({column:{key:a},record:e})=>[e.cells[a].type==="slot"?M(t.$slots,e.cells[a].key,{key:0,payload:e.cells[a].payload},void 0,!0):(n(),r(s(le),{key:1,open:e.cells[a].hover?void 0:!1},{content:l(()=>[c(s(P),{style:{width:"300px",overflow:"auto","font-family":"monospace"},copyable:"",content:e.cells[a].hover},null,8,["content"])]),default:l(()=>[e.cells[a].type==="text"?(n(),r(s($),{key:0,secondary:e.cells[a].secondary,code:e.cells[a].code},{default:l(()=>[y(f(e.cells[a].text),1)]),_:2},1032,["secondary","code"])):e.cells[a].type==="secret"?(n(),r(s($),{key:1,copyable:{text:e.cells[a].text}},{default:l(()=>[y(" ******** ")]),_:2},1032,["copyable"])):e.cells[a].type==="tag"?(n(),r(s(ce),{key:2,color:e.cells[a].tagColor},{default:l(()=>[y(f(e.cells[a].text),1)]),_:2},1032,["color"])):e.cells[a].type==="link"?(n(),r(V,{key:3,to:e.cells[a].to},{default:l(()=>[y(f(e.cells[a].text),1)]),_:2},1032,["to"])):e.cells[a].type==="actions"?(n(),r(s(K),{key:4},{overlay:l(()=>[c(s(ee),{disabled:u.value},{default:l(()=>[(n(!0),v(I,null,D(e.cells[a].actions.filter(o=>!o.hide),(o,b)=>(n(),r(s(te),{key:b,danger:o.dangerous,onClick:N=>m(o,e)},{default:l(()=>[_("div",De,[o.icon?(n(),r(ae(o.icon),{key:0})):h("",!0),c(s($),null,{default:l(()=>[y(f(o.label),1)]),_:2},1024)])]),_:2},1032,["danger","onClick"]))),128))]),_:2},1032,["disabled"])]),default:l(()=>[c(s(Ne),{style:{cursor:"pointer"},size:"25px"})]),_:2},1024)):h("",!0)]),_:2},1032,["open"]))]),footer:l(()=>[t.live?(n(),r(s(j),{key:0,justify:"end",gutter:10},{default:l(()=>[c(s(F),null,{default:l(()=>[c(s(ne),{size:"small"})]),_:1}),c(s(F),null,{default:l(()=>[c(s($),null,{default:l(()=>[y(" auto updating ")]),_:1})]),_:1})]),_:1})):h("",!0)]),_:3},8,["style","data-source","loading","columns"])]}),_:3}),t.fields?(n(),r(ze,{key:0,ref_key:"modalRef",ref:k,fields:t.fields,"entity-name":t.entityName,onCreate:Z},null,8,["fields","entity-name"])):h("",!0)],64)}}});const Le=oe(Pe,[["__scopeId","data-v-f0474cdf"]]);export{Le as C};
//# sourceMappingURL=CrudView.a5d66c2b.js.map
