import{d as f,eM as u,K as l,o as _,O as h,f as p,x as g}from"./outputWidgets.c7d11ead.js";import{E as m}from"./ExclamationCircleOutlined.276cec24.js";import{M as y}from"./Modal.7ab5d69d.js";(function(){try{var n=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},a=new Error().stack;a&&(n._sentryDebugIds=n._sentryDebugIds||{},n._sentryDebugIds[a]="7453cfb6-2c0c-4dd0-bbc8-de56f2ecae75",n._sentryDebugIdIdentifier="sentry-dbid-7453cfb6-2c0c-4dd0-bbc8-de56f2ecae75")}catch{}})();const c="You have unsaved changes. Are you sure you want to leave?",b=f({__name:"UnsavedChangesHandler",props:{hasChanges:{type:Boolean}},setup(n){const a=n,o=e=>(e=e||window.event,e&&(e.returnValue=c),c),i=()=>{window.addEventListener("beforeunload",o)};u(async(e,v,s)=>{if(!a.hasChanges)return s();await new Promise(r=>{y.confirm({title:"You have unsaved changes.",icon:p(m),content:"Are you sure you want to discard them?",okText:"Discard Changes",okType:"danger",cancelText:"Cancel",onOk(){r(!0)},onCancel(){r(!1)}})})?s():s(!1)});const t=()=>window.removeEventListener("beforeunload",o),d=e=>e?i():t();return l(()=>a.hasChanges,d),_(()=>d(a.hasChanges)),h(t),()=>{}}});const I=g(b,[["__scopeId","data-v-0a2660df"]]);export{I as U};
//# sourceMappingURL=UnsavedChangesHandler.97f6b632.js.map
