(function() {
    'use strict';
    
    window.WebFontConfig = {
        google: {
            families: ['Open+Sans:300,400:latin'],
        },

        active: function() {
            document.body.parentNode.classList.remove('wf-loading');
        },
    };

    var script = document.createElement('script');
    script.src = '//ajax.googleapis.com/ajax/libs/webfont/1.1.2/webfont.js';
    
    document.body.appendChild(script);
    
    window.setTimeout(window.WebFontConfig.active, 1000);
})();
