import{a as g}from"./asyncComputed.0d9bf0ef.js";import{d as y,eE as _,o as w,u as e,b as l,c as b,ew as x,f as a,w as o,as as p,bG as h,e as C,eH as I}from"./outputWidgets.c7d11ead.js";import{c}from"./router.95851ad5.js";import"./index.e05a5a2e.js";import{O as k}from"./organization.94de8fbd.js";import{L as v}from"./LoadingContainer.9fd2b01d.js";import{A}from"./Title.fdf5c01d.js";import{A as B}from"./index.8343729f.js";import{A as D}from"./index.bcace449.js";import{C as N}from"./Card.f339dcbe.js";import"./Form.894c92e7.js";import"./hasIn.dd565870.js";import"./popupNotifcation.ba1f83dd.js";import"./record.e5cfb835.js";import"./pubsub.a91a3d3f.js";import"./Base.984b27ce.js";import"./TabPane.4688ff0a.js";(function(){try{var t=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},n=new Error().stack;n&&(t._sentryDebugIds=t._sentryDebugIds||{},t._sentryDebugIds[n]="cc8d30fb-33ab-4083-9705-376de8a82d05",t._sentryDebugIdIdentifier="sentry-dbid-cc8d30fb-33ab-4083-9705-376de8a82d05")}catch{}})();const z={key:1},M={style:{display:"flex","justify-content":"flex-start","font-size":"24px"}},Y=y({__name:"Billing",setup(t){const r=_().params.organizationId,{loading:m,result:f}=g(()=>k.get(r));w(()=>{location.search.includes("upgrade")&&c.showNewMessage("I want to upgrade my plan")});const u=()=>c.showNewMessage("I want to upgrade my plan");return(E,V)=>e(m)?(l(),b(v,{key:0})):(l(),x("div",z,[a(e(B),{justify:"space-between",align:"center"},{default:o(()=>[a(e(A),{level:3},{default:o(()=>[p("Current plan")]),_:1})]),_:1}),a(e(D),{style:{"margin-top":"0"}}),a(e(N),{style:{width:"300px"},title:"Plan"},{extra:o(()=>[a(e(h),{onClick:u},{default:o(()=>[p("Upgrade")]),_:1})]),default:o(()=>{var s,i,d;return[C("div",M,I((d=(i=(s=e(f))==null?void 0:s.billingMetadata)==null?void 0:i.plan)!=null?d:"No active plan"),1)]}),_:1})]))}});export{Y as default};
//# sourceMappingURL=Billing.c228b32c.js.map
