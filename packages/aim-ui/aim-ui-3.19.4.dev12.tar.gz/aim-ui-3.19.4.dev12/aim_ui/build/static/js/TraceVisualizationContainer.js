(this.webpackJsonpui_v2=this.webpackJsonpui_v2||[]).push([[23],{1004:function(e,t,n){},1006:function(e,t,n){"use strict";n.d(t,"a",(function(){return l}));var a=n(6),i=n(72),r=n(32),o=n(134);function l(e){var t=e.data,n=e.groupingSelectOptions,l=e.model,s=e.defaultGroupFields;if(!i.a.isEmpty(t)){var c=null===l||void 0===l?void 0:l.getState(),d=null===c||void 0===c?void 0:c.config,u=null===d||void 0===d?void 0:d.grouping,p={},v=Object(a.a)((null===u||void 0===u?void 0:u.row)||[]),f=s||v,b={};return t.forEach((function(e){var t=null===f||void 0===f?void 0:f.reduce((function(t,l,s){var c=i.a.get(e.data[0],l);return i.a.set(b,t.concat(["ordering"]),new Set([].concat(Object(a.a)(i.a.get(b,t.concat(["ordering"]))||[]),[c]))),i.a.set(b,t.concat(["key"]),Object(o.a)(n,l)),i.a.set(b,t.concat(["orderKey"]),l),t.push("".concat(Object(o.a)(n,l)," = ").concat(Object(r.a)(c))),t}),[]);i.a.set(p,t,i.a.sortBy(e.data,[].concat(Object(a.a)(f),Object(a.a)(n.map((function(e){return e.value})).filter((function(e){return!f.includes(e)}))),["caption"])))})),{mediaSetData:i.a.isEmpty(p)?t[0].data:p,orderedMap:b}}return{}}},1319:function(e,t,n){"use strict";var a=n(0),i=n.n(a),r=n(72),o=n(777),l=n(5),s=(n(1004),n(1));function c(e){var t=e.onApply,n=e.applyButtonDisabled,a=e.onRangeSliderChange,c=e.onInputChange,d=e.items;return Object(s.jsx)("form",{className:"RangePanel",onSubmit:function(e){e.preventDefault(),t()},children:Object(s.jsxs)("div",{className:"RangePanelContainer",children:[null===d||void 0===d?void 0:d.map((function(e){var n,d,u,p,v,f,b,m,h,g=r.a.range(null!==(n=null===(d=e.rangeEndpoints)||void 0===d?void 0:d[0])&&void 0!==n?n:0,(null!==(u=null===(p=e.rangeEndpoints)||void 0===p?void 0:p[1])&&void 0!==u?u:0)+1).length;return Object(s.jsxs)(i.a.Fragment,{children:[(null===(v=e.rangeEndpoints)||void 0===v?void 0:v[0])!==(null===(f=e.rangeEndpoints)||void 0===f?void 0:f[1])?Object(s.jsx)(o.a,{sliderType:null===e||void 0===e?void 0:e.sliderType,sliderTitle:e.sliderTitle,countInputTitle:e.inputTitle,countTitleTooltip:e.inputTitleTooltip,sliderTitleTooltip:e.sliderTitleTooltip,min:null===(b=e.rangeEndpoints)||void 0===b?void 0:b[0],max:null===(m=e.rangeEndpoints)||void 0===m?void 0:m[1],selectedRangeValue:e.selectedRangeValue,selectedCountValue:e.inputValue,onSearch:t,onRangeChange:function(t){return a(e.sliderName,t)},onCountChange:function(t,n){c(e.inputName,t,n)},inputValidationPatterns:null!==(h=null===e||void 0===e?void 0:e.inputValidationPatterns)&&void 0!==h?h:[{errorCondition:function(e){return+e<=0},errorText:"Value should be greater then ".concat(0)},{errorCondition:function(e){return+e>g},errorText:"Value should be smaller then ".concat(g+1)}]}):Object(s.jsxs)("div",{className:"InfoMassageBox",children:[Object(s.jsx)(l.f,{name:"circle-info",color:"#1473E6"}),Object(s.jsxs)(l.n,{size:11,tint:80,weight:500,children:["You have only",Object(s.jsxs)(l.n,{size:11,tint:80,weight:600,className:"InfoMessageBoldText",children:["1 ",(null===e||void 0===e?void 0:e.infoPropertyName)||"step"]}),"logged."]})]}),Object(s.jsx)("div",{className:"VerticalDivider"})]},e.sliderName)})),Object(s.jsx)("div",{className:"ApplyButtonContainer",children:Object(s.jsx)(l.c,{size:"small",color:"primary",variant:"contained",type:"submit",className:"ApplyButton",disabled:n,children:"Apply"})})]})})}c.displayName="RangePanel";var d=i.a.memo(c);t.a=d},1358:function(e,t,n){"use strict";(function(e){n.d(t,"b",(function(){return b})),n.d(t,"c",(function(){return m})),n.d(t,"e",(function(){return h})),n.d(t,"h",(function(){return g})),n.d(t,"f",(function(){return y})),n.d(t,"d",(function(){return j})),n.d(t,"i",(function(){return x})),n.d(t,"g",(function(){return T})),n.d(t,"a",(function(){return _}));var a=n(2),i=n(6),r=n(416),o=n.n(r),l=n(72),s=n(97),c=n(178),d=n(20),u=n(98),p=n(1006),v=n(51),f=n(174);function b(e,t){for(var n="",a="",i={},r=0;r<e.length;r++)t.includes(n)?a+=e[r]:n+=e[r];return n=o.a.decode(n).toString(),a&&(i=JSON.parse(o.a.decode(a.substring(1,a.length)).toString())),{name:n,context:i}}function m(t,n){var a=_[t],r="",l="",d=function(t){var n=[],a=[],r=Object(c.a)({orderBy:"name",additionalCompare:function(e,t){return"EMPTY CONTEXT"===t?0:null}});return t.forEach((function(t){var l=o.a.encode(e.from("".concat(t.name))),c={name:t.name,id:l};if(t.context)if(Object.keys(t.context).length){var d=[],u={name:"".concat(Object(s.a)(t.context)),id:o.a.encode(e.from(JSON.stringify(t.context)))};d.push(u),c.children=d}else c.children=[{name:"empty context",id:o.a.encode(e.from(JSON.stringify({})))}];n.includes(l)?a.forEach((function(e,t){if(e.id===l){var n=a[t].children||[],o=c.children||[];a[t].children=[].concat(Object(i.a)(o),Object(i.a)(n)).sort(r),a[t].children.length||delete a[t].children}})):(a.push(c),n.push(l))})),a.sort(r),{availableIds:n,data:a}}(n),u=d.data,p=d.availableIds;return u[0].children&&u[0].children.length?(r=u[0].id+"."+u[0].children[0].id,l=u[0].children[0].name):(r=u[0].id+"",l=u[0].name),{data:u,defaultActiveKey:r,availableIds:p,title:a,defaultActiveName:l}}function h(e){var t=e.record_range_total,n=e.iters,r=e.values,o=[],l=[];return r&&r.forEach((function(e){for(var t=Object(i.a)(Object(v.b)(e.data.blob)),n=[],r=e.range[0],s=(e.range[1]-r)/e.bin_count,c=0;c<=e.bin_count;c++)n.push(r+c*s);o.push([t,n]),l.push(Object(a.a)(Object(a.a)({},e),{},{data:{blob:t}}))})),{iters:n,record_range:[null===t||void 0===t?void 0:t[0],((null===t||void 0===t?void 0:t[1])||0)-1],processedValues:o,originalValues:l,processedDataType:_.distributions}}function g(e){var t=e.record_range_total,n=e.index_range_total,a=e.iters,i=e.values,r=[];if(i){var o=0;i.forEach((function(e,t){e.forEach((function(e){r.push({step:null===a||void 0===a?void 0:a[t],index:e.index,text:e.data,key:o}),o++}))}))}return{iters:a,record_range:[null===t||void 0===t?void 0:t[0],((null===t||void 0===t?void 0:t[1])||0)-1],index_range:[null===n||void 0===n?void 0:n[0],((null===n||void 0===n?void 0:n[1])||0)-1],processedValues:l.a.orderBy(r,["step"],["desc"]),processedDataType:_.texts}}function y(e,t){var n=e.record_range_total,i=e.iters,r=e.values,o=e.index_range_total,s=e.context,c=e.name,v=t?Object(f.a)({params:Object(u.a)(t,t),sequenceName:"images"}):[],b=[];null===r||void 0===r||r.forEach((function(e,t){e.forEach((function(e){var n=Object(d.c)({name:c,traceContext:s,index:e.index,step:null===i||void 0===i?void 0:i[t],caption:e.caption}),r=Object(d.c)({name:c,traceContext:s});b.push(Object(a.a)(Object(a.a)({},e),{},{name:c,step:null===i||void 0===i?void 0:i[t],context:s,key:n,seqKey:r}))}))}));var m=Object(p.a)({data:O(l.a.orderBy(b)),groupingSelectOptions:v,defaultGroupFields:["step"]});return{imageSetData:m.mediaSetData,orderedMap:m.orderedMap,record_range:[null===n||void 0===n?void 0:n[0],((null===n||void 0===n?void 0:n[1])||0)-1],index_range:[null===o||void 0===o?void 0:o[0],((null===o||void 0===o?void 0:o[1])||0)-1],processedDataType:_.images}}function j(e,t){var n=e.record_range_total,i=e.iters,r=e.values,o=e.index_range_total,s=e.context,c=e.name,v=t?Object(f.a)({params:Object(u.a)(t,t),sequenceName:"audios"}):[],b=[];null===r||void 0===r||r.forEach((function(e,t){e.forEach((function(e){var n=Object(d.c)({name:c,traceContext:s,index:e.index,step:null===i||void 0===i?void 0:i[t],caption:e.caption}),r=Object(d.c)({name:c,traceContext:s});b.push(Object(a.a)(Object(a.a)({},e),{},{audio_name:c,step:null===i||void 0===i?void 0:i[t],context:s,key:n,seqKey:r}))}))}));var m=Object(p.a)({data:O(l.a.orderBy(b)),groupingSelectOptions:v,defaultGroupFields:["step"]});return{audiosSetData:m.mediaSetData,orderedMap:m.orderedMap,record_range:[null===n||void 0===n?void 0:n[0],((null===n||void 0===n?void 0:n[1])||0)-1],index_range:[null===o||void 0===o?void 0:o[0],((null===o||void 0===o?void 0:o[1])||0)-1],processedDataType:_.audios}}function O(e){for(var t={},n=function(n){var a={};["step"].forEach((function(t){a[t]=Object(v.d)(e[n],t)}));var i=Object(d.c)(a);t.hasOwnProperty(i)?t[i].data.push(e[n]):t[i]={key:i,config:a,data:[e[n]]}},a=0;a<e.length;a++)n(a);return Object.values(t)}function x(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t={};return Object.keys(e).forEach((function(n){var a=e[n];t[n]="".concat(a[0],":").concat(a[1]+1)})),t}function T(e){var t,n,a=e.record_range_total,i=e.iters,r=e.values,o=null,s=null;(null===(t=l.a.head(r))||void 0===t?void 0:t.data)?(s=r,(o=JSON.parse(null===(n=l.a.head(r))||void 0===n?void 0:n.data)).layout.autosize=!0):(o={},s=[]);return{iters:i,record_range:[null===a||void 0===a?void 0:a[0],((null===a||void 0===a?void 0:a[1])||0)-1],processedValue:o,originalValues:s,processedDataType:_.figures}}var _={images:"Images",distributions:"Distributions",audios:"Audios",videos:"Videos",texts:"Texts",figures:"Plotly"}}).call(this,n(179).Buffer)},1555:function(e,t,n){},1592:function(e,t,n){"use strict";n.r(t);var a=n(0),i=n.n(a),r=n(279),o=n(288),l=n(11),s=n(387),c=n(1319),d=n(17),u=n(8),p=n.n(u),v=n(7),f=n(4),b=n(27),m=n(2),h=n(72),g=n(281),y=n(78),j=n(14),O=n(146),x=n(1358),T={distributions:{dataProcessor:x.e,sliders:{record_range:{defaultValue:[0,50],title:"Steps",tooltip:"Training step. Increments every time track() is called",sliderType:"range",infoPropertyName:"step"}},inputs:{record_density:{defaultValue:50,title:"Steps",tooltip:"Number of steps to display"}}},images:{dataProcessor:x.f,sliders:{record_range:{defaultValue:[0,50],tooltip:"Training step. Increments every time track() is called",title:"Steps",sliderType:"range",infoPropertyName:"step"},index_range:{defaultValue:[0,50],tooltip:"Index in the list of images passed to track() call",title:"Indices",sliderType:"range",infoPropertyName:"index"}},inputs:{record_density:{defaultValue:50,title:"Steps count",tooltip:"Number of steps to display"},index_density:{defaultValue:5,title:"Indices count",tooltip:"Number of images per step"}}},audios:{dataProcessor:x.d,sliders:{record_range:{defaultValue:[0,50],tooltip:"Training step. Increments every time track() is called",title:"Steps",sliderType:"range",infoPropertyName:"step"},index_range:{defaultValue:[0,50],tooltip:"Index in the list of audios passed to track() call",title:"Indices",sliderType:"range",infoPropertyName:"index"}},inputs:{record_density:{defaultValue:50,title:"Steps count",tooltip:"Number of steps to display"},index_density:{defaultValue:5,title:"Indices count",tooltip:"Number of audios per step"}}},texts:{dataProcessor:x.h,sliders:{record_range:{defaultValue:[0,50],tooltip:"Training step. Increments every time track() is called",title:"Steps",sliderType:"range",infoPropertyName:"step"},index_range:{defaultValue:[0,50],tooltip:"Index in the list of texts passed to track() call",title:"Indices",sliderType:"range",infoPropertyName:"index"}},inputs:{record_density:{defaultValue:50,title:"Steps count",tooltip:"Number of steps to display"},index_density:{defaultValue:5,title:"Indices count",tooltip:"Number of texts per step"}}},figures:{dataProcessor:x.g,paramsToApi:function(e){var t,n,a=null!==(t=null===e||void 0===e||null===(n=e.inputs)||void 0===n?void 0:n.record_range)&&void 0!==t?t:-1;return-1!==a?{record_step:a,record_density:1}:{record_density:1}},inputValidation:function(e,t){return[{errorCondition:function(t){return+t<e},errorText:"Value should be equal or greater then ".concat(e)},{errorCondition:function(e){return+e>t},errorText:"Value should be equal or smaller then ".concat(t)}]},sliders:{record_range:{defaultValue:[0,0],tooltip:"Training step. Increments every time track() is called",title:"Step",sliderType:"single",infoPropertyName:"step"}},inputs:{record_range:{defaultValue:-1,tooltip:"Training step. To see figures tracked in the step.",title:"Step"}}}};function _(e){var t,n,a,i=2;for("undefined"!=typeof Symbol&&(n=Symbol.asyncIterator,a=Symbol.iterator);i--;){if(n&&null!=(t=e[n]))return t.call(e);if(a&&null!=(t=e[a]))return new N(t.call(e));n="@@asyncIterator",a="@@iterator"}throw new TypeError("Object is not async iterable")}function N(e){function t(e){if(Object(e)!==e)return Promise.reject(new TypeError(e+" is not an object."));var t=e.done;return Promise.resolve(e.value).then((function(e){return{value:e,done:t}}))}return(N=function(e){this.s=e,this.n=e.next}).prototype={s:null,n:null,next:function(){return t(this.n.apply(this.s,arguments))},return:function(e){var n=this.s.return;return void 0===n?Promise.resolve({value:e,done:!0}):t(n.apply(this.s,arguments))},throw:function(e){var n=this.s.return;return void 0===n?Promise.reject(e):t(n.apply(this.s,arguments))}},new N(e)}var V=null,S=Object(g.a)({});function I(e){var t=T[e],n={sliders:{},inputs:{},inputsValidations:{}},a={rangePanel:[]},i=Object.keys(null===t||void 0===t?void 0:t.inputs);return Object.keys(t.sliders).forEach((function(e,r){var o=t.sliders[e];n.sliders[e]=o.defaultValue;var l=t.inputs[i[r]],s={sliderName:e,inputName:i[r],sliderTitle:o.title,inputTitle:l.title,sliderTitleTooltip:o.tooltip,inputTitleTooltip:l.tooltip,sliderType:o.sliderType,inputValidationPatterns:t.inputValidation,infoPropertyName:null===o||void 0===o?void 0:o.infoPropertyName};a.rangePanel.push(s)})),Object.keys(t.inputs).forEach((function(e){n.inputs[e]=t.inputs[e].defaultValue})),{queryData:n,config:a}}function P(){var e;V&&(null===(e=V)||void 0===e||e.abort(),V=null)}function D(e,t){var n={};return t.forEach((function(t){n[t]=e[t]})),n}function k(){return C.apply(this,arguments)}function C(){return(C=Object(b.a)(p.a.mark((function e(){var t,n,a,i,r,o,l,s,c,d,u,b,g,j,N,I,k,C,E,A,B,q,w,z,R=arguments;return p.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=R.length>0&&void 0!==R[0]&&R[0],P(),n=S.getState(),a=n.traceType||"distributions",i=n.batchRequestOptions,r=n.queryData,(o=T[a].paramsToApi)||(o=function(e){return Object(m.a)(Object(m.a)({},t?{}:Object(x.i)(null===e||void 0===e?void 0:e.sliders)),null===e||void 0===e?void 0:e.inputs)}),V="figures"===a?y.a.getBatchByStep(n.runHash||"",a,o(r),[null===i||void 0===i?void 0:i.trace]):y.a.getBatch(n.runHash||"",a,o(r),[null===i||void 0===i?void 0:i.trace]),e.prev=9,S.setState(Object(m.a)(Object(m.a)({},n),{},{batchRequestOptions:Object(m.a)(Object(m.a)({},i),{},{params:r}),isTraceBatchLoading:!0})),e.next=13,null===(l=V)||void 0===l?void 0:l.call((function(e){console.error(e)}));case 13:s=e.sent,c=Object(O.a)(s),d=Object(O.b)(c),u=Object(O.c)(d,1),b={},g=!0,j=!1,e.prev=20,I=_(u);case 22:return e.next=24,I.next();case 24:return k=e.sent,g=k.done,e.next=28,k.value;case 28:if(C=e.sent,g){e.next=35;break}E=C,A=Object(v.a)(E,2),B=A[0],q=A[1],b=Object(m.a)(Object(m.a)({},b),{},Object(f.a)({},B[0],q));case 32:g=!0,e.next=22;break;case 35:e.next=41;break;case 37:e.prev=37,e.t0=e.catch(20),j=!0,N=e.t0;case 41:if(e.prev=41,e.prev=42,g||null==I.return){e.next=46;break}return e.next=46,I.return();case 46:if(e.prev=46,!j){e.next=49;break}throw N;case 49:return e.finish(46);case 50:return e.finish(41);case 51:w=T[n.traceType||"distributions"].dataProcessor(b,null===n||void 0===n?void 0:n.runParams),t&&(z=D(w,Object.keys((null===r||void 0===r?void 0:r.sliders)||{})),r&&(r.sliders=z,Object.keys(r.inputs).forEach((function(e){var t,n=e.slice(0,e.indexOf("_")),a=w["".concat(n,"_range")];if(w.processedDataType===x.a.figures&&(r.inputs[e]<a[0]||r.inputs[e]>a[1]))r.inputs[e]=null!==(t=a[1])&&void 0!==t?t:1;else if(w.processedDataType!==x.a.figures&&r.inputs[e]<0||r.inputs[e]>a[1]){var i=h.a.range(a[0],a[1]+1).length;r.inputs[e]=i>0?i:1}else{var o;r.inputs[e]=null!==(o=r.inputs[e])&&void 0!==o?o:1}})))),S.setState(Object(m.a)(Object(m.a)({},n),{},{data:w,queryData:r,isTraceBatchLoading:!1,isTraceContextBatchLoading:!1})),e.next=60;break;case 56:throw e.prev=56,e.t1=e.catch(9),S.setState(Object(m.a)(Object(m.a)({},n),{},{isTraceBatchLoading:!1})),e.t1;case 60:case"end":return e.stop()}}),e,null,[[9,56],[20,37,41,51],[42,,46,50]])})))).apply(this,arguments)}function E(){var e,t=S.getState(),n=(null===(e=t.queryData)||void 0===e?void 0:e.inputsValidations)||{},a=h.a.size(Object.keys(n).filter((function(e){return!n[e]})))<=0;S.setState(Object(m.a)(Object(m.a)({},t),{},{isApplyBtnDisabled:!a}))}var A=Object(m.a)(Object(m.a)({},S),{},{destroy:function(){S.destroy(),P()},onApply:function(){var e=S.getState().traceType;k().then().catch(),Object(j.b)(d.a.runDetails.tabs[e].clickApplyButton)},initialize:function(e,t,n,a){S.init();var i=Object(x.c)(t,n),r=i.data,o=i.availableIds,l=i.title,s=i.defaultActiveKey,c=i.defaultActiveName,d=I(t),u=d.queryData,p=d.config;S.setState({config:p,queryData:u,isApplyBtnDisabled:!1,traceType:t,runHash:e,isTraceBatchLoading:!0,runParams:a,menu:{title:l,items:r,defaultActiveItemKey:s,activeItemKey:s,availableKeys:o,activeItemName:c},batchRequestOptions:{trace:Object(x.b)(s,o),query:null}}),k(!0).then().catch()},onInputChange:function(e,t){var n,a,i=!(arguments.length>2&&void 0!==arguments[2])||arguments[2],r=S.getState();S.setState(Object(m.a)(Object(m.a)({},r),{},{queryData:Object(m.a)(Object(m.a)({},r.queryData),{},{inputs:Object(m.a)(Object(m.a)({},null===(n=r.queryData)||void 0===n?void 0:n.inputs),{},Object(f.a)({},e,t)),inputsValidations:Object(m.a)(Object(m.a)({},null===(a=r.queryData)||void 0===a?void 0:a.inputsValidations),{},Object(f.a)({},e,i))})})),E()},onRangeChange:function(e,t){var n,a=S.getState();S.setState(Object(m.a)(Object(m.a)({},a),{},{queryData:Object(m.a)(Object(m.a)({},a.queryData),{},{sliders:Object(m.a)(Object(m.a)({},null===(n=a.queryData)||void 0===n?void 0:n.sliders),{},Object(f.a)({},e,t))})}))},changeActiveItemKey:function(e,t){var n=S.getState(),a=n.menu,i=n.batchRequestOptions,r=n.traceType||"distributions",o=Object(x.b)(e||"",(null===a||void 0===a?void 0:a.availableKeys)||[]);S.setState(Object(m.a)(Object(m.a)(Object(m.a)({},n),I(r)),{},{isTraceContextBatchLoading:!0,menu:Object(m.a)(Object(m.a)({},a),{},{activeItemKey:e,activeItemName:t}),batchRequestOptions:Object(m.a)(Object(m.a)({},i),{},{trace:o})})),k(!0).then().catch(),Object(j.b)(d.a.runDetails.tabs[n.traceType].changeActiveItemKey)}}),B=n(370),q=n(208),w=n(1);var z=function(e){return function(t){var n=(null===t||void 0===t?void 0:t.traceInfo)?null===t||void 0===t?void 0:t.traceInfo[t.traceType]:null,a="No tracked ".concat(t.traceType);return n&&n.length?Object(w.jsx)(e,Object(m.a)({},t)):Object(w.jsx)(B.a,{size:"xLarge",className:"TraceEmptyVisualizer",type:q.c.EmptyData,title:a})}},R=(n(1555),i.a.lazy((function(){return Promise.all([n.e(39),n.e(11)]).then(n.bind(null,1595))}))),K=i.a.lazy((function(){return Promise.all([n.e(3),n.e(13)]).then(n.bind(null,1602))})),L=i.a.lazy((function(){return n.e(22).then(n.bind(null,1603))})),W=i.a.lazy((function(){return Promise.all([n.e(8),n.e(14)]).then(n.bind(null,1604))})),M={images:K,distributions:R,audios:i.a.lazy((function(){return Promise.all([n.e(3),n.e(10)]).then(n.bind(null,1599))})),videos:function(){return null},texts:L,figures:W};function J(e){var t,n,a,u,p,v,f=e.traceInfo,b=e.traceType,m=e.runHash,h=e.runParams,g=Object(r.a)(A);i.a.useEffect((function(){return A.initialize(m,b,f[b],h),function(){A.destroy()}}),[m,f,b]);var y=M[b];return i.a.useEffect((function(){j.a(d.a.runDetails.tabs[b].tabView)}),[b]),Object(w.jsx)(l.a,{children:Object(w.jsxs)("div",{className:"TraceVisualizationWrapper",children:[Object(w.jsx)("div",{className:"MenuArea",children:(null===g||void 0===g||null===(t=g.menu)||void 0===t?void 0:t.defaultActiveItemKey)&&Object(w.jsx)(o.a,{defaultActiveItemKey:null===g||void 0===g||null===(n=g.menu)||void 0===n?void 0:n.defaultActiveItemKey,onChangeActiveItem:A.changeActiveItemKey,title:null===g||void 0===g||null===(a=g.menu)||void 0===a?void 0:a.title,data:(null===g||void 0===g||null===(u=g.menu)||void 0===u?void 0:u.items)||[]})}),Object(w.jsxs)("div",{className:"VisualizerArea",children:[Object(w.jsx)(i.a.Suspense,{fallback:Object(w.jsx)("div",{className:"VisualizerArea__suspenseLoaderContainer",children:Object(w.jsx)(s.a,{})}),children:Object(w.jsx)(y,{data:null===g||void 0===g?void 0:g.data,isLoading:null===g||void 0===g?void 0:g.isTraceBatchLoading,activeTraceContext:null===g||void 0===g||null===(p=g.menu)||void 0===p?void 0:p.activeItemName})}),(null===g||void 0===g?void 0:g.data)&&(null===g||void 0===g?void 0:g.config)&&!(null===g||void 0===g?void 0:g.isTraceContextBatchLoading)&&(null===g||void 0===g?void 0:g.queryData)&&Object(w.jsx)(c.a,{items:null===g||void 0===g||null===(v=g.config)||void 0===v?void 0:v.rangePanel.map((function(e){var t,n,a;return{key:e.sliderName,sliderName:e.sliderName,inputName:e.inputName,sliderTitle:e.sliderTitle,inputTitle:e.inputTitle,sliderTitleTooltip:e.sliderTitleTooltip,inputTitleTooltip:e.inputTitleTooltip,rangeEndpoints:null===g||void 0===g?void 0:g.data[e.sliderName],selectedRangeValue:(null===g||void 0===g||null===(t=g.queryData)||void 0===t?void 0:t.sliders[e.sliderName])||[0,0],inputValue:(null===g||void 0===g||null===(n=g.queryData)||void 0===n?void 0:n.inputs[e.inputName])||0,sliderType:e.sliderType,inputValidationPatterns:null===(a=e.inputValidationPatterns)||void 0===a?void 0:a.call(e,null===g||void 0===g?void 0:g.data[e.sliderName][0],null===g||void 0===g?void 0:g.data[e.sliderName][1]),infoPropertyName:null===e||void 0===e?void 0:e.infoPropertyName}})),onApply:A.onApply,onInputChange:function(e,t,n){return function(e,t,n){A.onInputChange(e,t,null===n||void 0===n?void 0:n.isValid)}(e,t,n)},onRangeSliderChange:A.onRangeChange,applyButtonDisabled:!!(null===g||void 0===g?void 0:g.isTraceBatchLoading)||!!(null===g||void 0===g?void 0:g.isApplyBtnDisabled)})]})]})})}J.displayName="TraceVisualizationContainer";var H=i.a.memo(z(J));t.default=H},769:function(e,t,n){},777:function(e,t,n){"use strict";var a=n(6),i=n(0),r=n.n(i),o=n(353),l=n(5),s=n(11),c=(n(769),n(1));function d(e){var t=e.sliderTitle,n=e.countInputTitle,i=e.selectedRangeValue,r=e.selectedCountValue,d=e.onSearch,u=e.onCountChange,p=e.onRangeChange,v=e.min,f=e.max,b=e.sliderTitleTooltip,m=e.countTitleTooltip,h=e.sliderType,g=void 0===h?"range":h,y=e.inputValidationPatterns;return Object(c.jsx)(s.a,{children:Object(c.jsxs)("div",{className:"SliderWithInput",children:[Object(c.jsxs)("div",{className:"SliderWithInput__sliderWrapper",children:[Object(c.jsxs)("div",{className:"SliderWithInput__sliderWrapper__sliderTitleBox",children:[b?Object(c.jsx)(o.a,{title:b,children:Object(c.jsxs)("span",{className:"SliderWithInput__sliderWrapper__title",children:[t,":"]})}):Object(c.jsxs)("span",{className:"SliderWithInput__sliderWrapper__title",children:[t,":"]}),Object(c.jsx)(l.n,{size:10,weight:600,tint:80,className:"SliderWithInput__sliderWrapper__sliderValuesLabel",children:"".concat(i[0]," - ").concat(i[1])})]}),"single"===g?Object(c.jsx)(l.k,{value:r,onChange:function(e,t){u(t)},getAriaValueText:function(e){return"".concat(e)},"aria-labelledby":"track-false-slider",track:!1,min:i[0],max:i[1],valueLabelDisplay:"auto"}):Object(c.jsx)(l.k,{value:Object(a.a)(i),onChange:function(e,t){return p(t)},min:v,max:f,valueLabelDisplay:"auto",getAriaValueText:function(e){return"".concat(e)},onKeyPress:function(e){13===e.which&&d()}})]}),Object(c.jsx)("div",{className:"SliderWithInput__densityWrapper",children:Object(c.jsx)(l.g,{value:"".concat(r),type:"number",labelAppearance:"top-labeled",size:"small",label:n,topLabeledIconName:"circle-question",labelHelperText:m,placeholder:n,showMessageByTooltip:!0,isValidateInitially:!0,onChange:function(e,t,n){u(t,n)},validationPatterns:null!==y&&void 0!==y?y:[]})})]})})}d.displayName="SliderWithInput";var u=r.a.memo(d);t.a=u}}]);
//# sourceMappingURL=TraceVisualizationContainer.js.map?version=be63ee7c3421b6f193cd