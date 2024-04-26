var U=Object.defineProperty;var N=(d,e,i)=>e in d?U(d,e,{enumerable:!0,configurable:!0,writable:!0,value:i}):d[e]=i;var w=(d,e,i)=>(N(d,typeof e!="symbol"?e+"":e,i),i);import{I as T,K as S,eO as V,d as $,eE as q,b as u,c as y,w as o,u as t,f as n,as as m,af as L,bh as k,cC as C,ew as x,eF as O,eH as b,e as K,aE as D,ex as Q,ck as z,ey as H,bD as G}from"./outputWidgets.c7d11ead.js";import{a as j,A}from"./router.95851ad5.js";import{a as J,b as M,g as W}from"./datetime.685f1a28.js";import"./index.e05a5a2e.js";import{E as X,_ as Y}from"./ExecutionStatusIcon.vue_vue_type_script_setup_true_lang.3e8e9e2d.js";import{h as B}from"./index.c8b526e4.js";import{R as Z}from"./dayjs.881a974e.js";import{A as tt}from"./Title.fdf5c01d.js";import{A as E,F as et}from"./Form.894c92e7.js";import{A as at,C as st}from"./CollapsePanel.b78c52e8.js";import{A as P}from"./index.e53fe664.js";import"./popupNotifcation.ba1f83dd.js";import"./record.e5cfb835.js";import"./pubsub.a91a3d3f.js";import"./LoadingOutlined.656209b9.js";import"./Base.984b27ce.js";import"./hasIn.dd565870.js";(function(){try{var d=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},e=new Error().stack;e&&(d._sentryDebugIds=d._sentryDebugIds||{},d._sentryDebugIds[e]="b15c7bb9-1a86-4927-b365-80f089845583",d._sentryDebugIdIdentifier="sentry-dbid-b15c7bb9-1a86-4927-b365-80f089845583")}catch{}})();class it{constructor(e,i,l,c,f,p){w(this,"state");w(this,"handleFilterChange",()=>{this.state.currentPage.waitingDebounce=!0,this.state.pagination.currentIndex=1,this.debouncedPageRefetch()});w(this,"debouncedPageRefetch",V.exports.debounce(async()=>{await this.fetchPage(),this.state.currentPage.waitingDebounce=!1},500));w(this,"fetchEmptyLogs",()=>{this.state.currentPage.openedExecutionIds.forEach(async e=>{!this.state.currentPage.loadedLogs[e]&&await this.fetchLogs(e)})});this.executionRepository=e,this.buildRepository=i,this.projectId=l,this.state=T({currentPage:{openedExecutionIds:p?[p]:[],loadingExecutions:!1,waitingDebounce:!1,executions:[],loadedLogs:{}},pagination:{currentIndex:1,pageSize:10,totalCount:0,...f},filters:{dateRange:void 0,buildId:void 0,stageId:void 0,...c},filterOptions:{builds:[],stages:[]}}),S(()=>this.state.filters.buildId,()=>{this.fetchStageOptions()}),S(this.state.filters,()=>{this.state.currentPage.openedExecutionIds=[],this.handleFilterChange()}),S(()=>this.state.pagination.currentIndex,()=>{this.state.currentPage.openedExecutionIds=[],this.fetchPage()})}async init(){await Promise.all([this.fetchPage(),this.fetchOptions()]),this.fetchEmptyLogs(),this.setupRefetchInterval()}async fetchPage(){var l,c,f,p;this.state.currentPage.loadingExecutions=!0;const{executions:e,totalCount:i}=await this.executionRepository.list({projectId:this.projectId,buildId:this.state.filters.buildId,limit:this.state.pagination.pageSize,offset:(this.state.pagination.currentIndex-1)*this.state.pagination.pageSize,stageId:this.state.filters.stageId,startDate:(c=(l=this.state.filters.dateRange)==null?void 0:l[0])==null?void 0:c.toISOString(),endDate:(p=(f=this.state.filters.dateRange)==null?void 0:f[1])==null?void 0:p.toISOString()});this.state.currentPage.loadingExecutions=!1,this.state.currentPage.executions=e,this.state.pagination.totalCount=i}async fetchBuildOptions(){const i=(await this.buildRepository.list(this.projectId)).map(l=>({label:`[${l.id.slice(0,8)}] ${l.createdAt.toLocaleString()} ${l.latest?"(Latest)":""}`,value:l.id}));this.state.filterOptions.builds=i}async fetchStageOptions(){var l;const e=await J.get((l=this.state.filters.buildId)!=null?l:this.state.filterOptions.builds[0].value),i=e==null?void 0:e.runtimes.map(c=>({label:c.title,value:c.id}));this.state.filterOptions.stages=i!=null?i:[]}async fetchOptions(){await this.fetchBuildOptions(),await this.fetchStageOptions()}async fetchLogs(e){const i=await this.executionRepository.fetchLogs(this.projectId,e);this.state.currentPage.loadedLogs[e]=i}async setupRefetchInterval(){setTimeout(async()=>{await Promise.all(this.state.currentPage.openedExecutionIds.map(e=>this.fetchLogs(e))),this.setupRefetchInterval()},1e3)}}const nt={style:{width:"100px",height:"100%",display:"flex","align-items":"center","justify-content":"right",gap:"10px"}},ot={key:0,style:{display:"flex",width:"100%","justify-content":"center"}},rt={key:1,style:{"background-color":"#555","border-radius":"5px",padding:"10px",color:"#fff","font-family":"monospace","max-height":"600px",overflow:"auto"}},St=$({__name:"Logs",setup(d){const e=new X,i=new M,l=q(),c=l.params.projectId,f=l.query.executionId;function p(){const{stageId:h,buildId:r,startDate:a,endDate:g}=l.query;return a&&g?{stageId:h,buildId:r,dateRange:[B(a),B(g)]}:{stageId:h,buildId:r}}function F(){const{page:h,pageSize:r}=l.query;return{page:h?parseInt(h,10):1,pageSize:r?parseInt(r,10):10}}const _=new it(e,i,c,p(),F(),f),{state:s}=_;return _.init(),(h,r)=>(u(),y(t(C),{direction:"vertical",style:{width:"100%"}},{default:o(()=>[n(t(tt),null,{default:o(()=>[m("Logs")]),_:1}),n(t(et),{layout:"vertical"},{default:o(()=>[n(t(j),{gutter:10},{default:o(()=>[n(t(A),{span:24},{default:o(()=>[n(t(E),{label:"Script"},{default:o(()=>[n(t(L),{value:t(s).filters.stageId,"onUpdate:value":r[0]||(r[0]=a=>t(s).filters.stageId=a),options:t(s).filterOptions.stages,placeholder:"All","allow-clear":""},null,8,["value","options"])]),_:1})]),_:1})]),_:1}),n(t(j),{gutter:10},{default:o(()=>[n(t(A),{span:12},{default:o(()=>[n(t(E),{label:"Date"},{default:o(()=>[n(t(Z),{value:t(s).filters.dateRange,"onUpdate:value":r[1]||(r[1]=a=>t(s).filters.dateRange=a),style:{width:"100%"}},null,8,["value"])]),_:1})]),_:1}),n(t(A),{span:12},{default:o(()=>[n(t(E),{label:"Build"},{default:o(()=>[n(t(L),{value:t(s).filters.buildId,"onUpdate:value":r[2]||(r[2]=a=>t(s).filters.buildId=a),options:t(s).filterOptions.builds,"option-label":"label","option-value":"value",filter:!1,placeholder:"All","allow-clear":""},null,8,["value","options"])]),_:1})]),_:1})]),_:1})]),_:1}),t(s).currentPage.loadingExecutions||t(s).currentPage.waitingDebounce?(u(),y(t(k),{key:0,style:{width:"100%"}})):t(s).currentPage.executions&&t(s).currentPage.executions.length>0?(u(),y(t(C),{key:1,direction:"vertical",style:{width:"100%"}},{default:o(()=>[n(t(st),{"active-key":t(s).currentPage.openedExecutionIds,"onUpdate:activeKey":r[3]||(r[3]=a=>t(s).currentPage.openedExecutionIds=a),bordered:!1,style:{"background-color":"transparent"},onChange:t(_).fetchEmptyLogs},{default:o(()=>[(u(!0),x(D,null,O(t(s).currentPage.executions,a=>(u(),y(t(at),{key:a.id,style:{"border-radius":"4px","margin-bottom":"10px",border:"0",overflow:"hidden","background-color":"#fff"}},{header:o(()=>[n(t(P),{color:"default",style:{"margin-right":"10px"},bordered:!1},{default:o(()=>[m(b(t(W)(a.createdAt)),1)]),_:2},1024),n(t(P),{color:"default",style:{"margin-right":"10px"},bordered:!1},{default:o(()=>[m(" Run ID: "+b(a.id.slice(0,8)),1)]),_:2},1024),n(t(P),{color:"default",style:{"margin-right":"10px"},bordered:!1},{default:o(()=>[m(" Build: "+b(a.buildId.slice(0,8)),1)]),_:2},1024),n(t(P),{color:"default",style:{"margin-right":"10px"},bordered:!1},{default:o(()=>{var g,I;return[m(b((I=(g=t(s).filterOptions.stages.find(v=>v.value===a.stageId))==null?void 0:g.label)!=null?I:a.stageId.slice(0,8)),1)]}),_:2},1024)]),extra:o(()=>[K("div",nt,[m(b(a.status.charAt(0).toUpperCase()+a.status.slice(1))+" ",1),n(Y,{status:a.status},null,8,["status"])])]),default:o(()=>{var g,I,v;return[t(s).currentPage.loadedLogs[a.id]?(g=t(s).currentPage.loadedLogs[a.id])!=null&&g.entries.length?(u(),x("div",rt,[(u(!0),x(D,null,O((I=t(s).currentPage.loadedLogs[a.id])==null?void 0:I.entries,R=>(u(),x("p",{key:R.createdAt,style:Q({margin:0,"white-space":"pre-wrap",color:R.event==="unhandled-exception"?"rgb(255, 133, 133)":"inherit"})},b(R.payload.text.trim()),5))),128))])):(v=t(s).currentPage.loadedLogs[a.id])!=null&&v.entries.length?H("",!0):(u(),y(t(z),{key:2})):(u(),x("div",ot,[n(t(k))]))]}),_:2},1024))),128))]),_:1},8,["active-key","onChange"]),n(t(G),{current:t(s).pagination.currentIndex,"onUpdate:current":r[4]||(r[4]=a=>t(s).pagination.currentIndex=a),"page-size":t(s).pagination.pageSize,"onUpdate:pageSize":r[5]||(r[5]=a=>t(s).pagination.pageSize=a),total:t(s).pagination.totalCount,"show-size-changer":""},null,8,["current","page-size","total"])]),_:1})):(u(),y(t(z),{key:2}))]),_:1}))}});export{St as default};
//# sourceMappingURL=Logs.bedbe9af.js.map
