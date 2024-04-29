/*
 * This file will be inserted as the last child of the iframe's <body>
 */

var virtualClick = function(evnt) {
    // Handle GET parameters and anchors
    // console.log("Virtual click", evnt);

    var el = evnt.currentTarget;
    var name = el.tagName.toLowerCase();

    if (name == 'a') {
        var [path, getParameters, anchor] = splitUrl(el.getAttribute('href'));
    } else if (name == 'form') {
        var [path, getParameters, anchor] = splitUrl(el.getAttribute('action'));
        const formData = new FormData(el);
        getParameters = new URLSearchParams(formData).toString();
    } else {
        console.error("Invalid element", el);
    }

    path = normalizePath(path);

    window.parent.postMessage({
        action: "virtualClick",
        argument: {
            path: path,
            getParameters: getParameters,
            anchor: anchor,
        }
    }, '*');
    evnt.preventDefault();
    evnt.stopPropagation();
    return false;
};


var onScrollToAnchor = function() {
    if (window.globalContext.anchor) {
        document.location.replace("about:srcdoc#" + window.globalContext.anchor);
    }
}


var monkeyPatch = function() {
    if (typeof jQuery === 'undefined') {return;} // Only for jQuery at the moment
    /**
     * Monkey patch getQueryParameters
     * This function is defined in Sphinx' (v4) doctools.js and incompatible with our
     * approach.
     * This is a copy with effectively only the third line changed.
     * See: https://github.com/sphinx-doc/sphinx/blob/2329fdef8c20c6c75194f5d842b8f62ebad5c79d/sphinx/themes/basic/static/doctools.js#L54
     */
    jQuery._getQueryParameters = jQuery.getQueryParameters;
    jQuery.getQueryParameters = function(s) {
      if (typeof s === 'undefined')
        s = '?' + window.globalContext.getParameters;
      return jQuery._getQueryParameters(s);
    };

    /**
     * Monkey patch jQuery.ajax
     * Only settings.url and settings.complete are supported for virtual
     * URLs.
     */
    jQuery._ajax = jQuery.ajax;
    jQuery.ajax = function(settings) {
        url = normalizePath(settings.url);
        if (isVirtual(url)) {
            var result;
            var data;
            data = retrieveFile(url);
            result = settings.complete({responseText: data}, "");
            return; // Return value not actually needed in searchtools.js
        } else {
            return jQuery.ajax(settings);
        };
    };
}

monkeyPatch();

// Set up message listener
window.addEventListener("message", (evnt) => {
    console.log("Received message in iframe", evnt.data);
    if (evnt.data.action == 'scrollToAnchor') {
        onScrollToAnchor(evnt.data.argument);
    }
}, false);

window.parent.postMessage({
    action: "ready",
}, '*');


document.addEventListener('keyup', function (event) {
    if (event.key == "Z" && event.ctrlKey){
        window.parent.postMessage({
            action: "showMenu",
        }, '*');
    }
});
