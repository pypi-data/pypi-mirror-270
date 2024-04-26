"use strict";
exports.id = 726;
exports.ids = [726];
exports.modules = {

/***/ 630970:
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Z": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var process__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(677282);
/* harmony import */ var process__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(process__WEBPACK_IMPORTED_MODULE_0__);

const localConfig = {
    apiUrl: `${process__WEBPACK_IMPORTED_MODULE_0__.env.KANGAS_BACKEND_PROTOCOL || "http"}://${process__WEBPACK_IMPORTED_MODULE_0__.env.KANGAS_BACKEND_HOST}:${process__WEBPACK_IMPORTED_MODULE_0__.env.KANGAS_BACKEND_PORT}/datagrid/`,
    rootUrl: `${process__WEBPACK_IMPORTED_MODULE_0__.env.KANGAS_FRONTEND_PROTOCOL || "http"}://${process__WEBPACK_IMPORTED_MODULE_0__.env.KANGAS_FRONTEND_HOST}:${process__WEBPACK_IMPORTED_MODULE_0__.env.PORT}${process__WEBPACK_IMPORTED_MODULE_0__.env.KANGAS_FRONTEND_ROOT || ""}/`,
    rootPath: `${process__WEBPACK_IMPORTED_MODULE_0__.env.KANGAS_FRONTEND_ROOT || ""}/`,
    defaultDecimalPrecision: null,
    locale: "en-US",
    hideSelector: process__WEBPACK_IMPORTED_MODULE_0__.env.KANGAS_HIDE_SELECTOR === "1",
    cache: true,
    prefetch: false,
    debug: false,
    dynamic: false
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (localConfig);


/***/ }),

/***/ 345261:
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Z": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
const formatQueryArgs = (obj)=>{
    return Object.entries(obj).filter(([key, value])=>typeof value !== "undefined" && value !== null).map(([key, value])=>{
        if (value !== null && typeof value === "object") {
            value = JSON.stringify(value);
        }
        return `${key}=${encodeURIComponent(`${value}`)}`;
    }).join("&");
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (formatQueryArgs);


/***/ })

};
;