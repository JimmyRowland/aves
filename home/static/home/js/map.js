// bingmaps.js
// ------------------------------------------------------------------
//
// logic to display interactive an map from bing.
//
// Author     : Dino
// Created    : Mon Aug 15 11:27:34 2011
// on Machine : DINO-PC
// Last-saved : <2011-August-17 19:08:04>
//
// ------------------------------------------------------------------

(function() {

    if (typeof bingMap === "undefined") {
        if (typeof String.prototype.trim === "undefined") {
            String.prototype.trim=function(){return this.replace(/^\s+|\s+$/g,""); };
        }

        var bingMapsKey = "AvLxw-lFso_wogNNBczW4pdX3OYpQlLD1BsCOyNcu7VswtnlDEIQ8VU32UsoVnlZ";
        //var directionsManager = null;

        // function eventHandler1 () {
        //   // see http://onlinehelp.microsoft.com/en-us/bing/ff808440.aspx
        //   window.open ("http://www.bing.com/maps/?v=2&cp=37.608696~-77.494041&lvl=10&style=r&where1=5904%20School%20Ave.%20Richmond,%20VA%2023228","rbaDirectionsWindow");
        // }

        // function eventHandler2 () {
        //   // see http://onlinehelp.microsoft.com/en-us/bing/ff808440.aspx
        //   window.open ("http://www.bing.com/maps/?v=2&cp=37.698233~-77.663426&lvl=10&style=r&where1=2318%20Commerce%20Center%20Drive%20Rockville,%20VA%2023146","rbaDirectionsWindow");
        // }

        var addPushpin = function( map, params ) {
            if (typeof params.location != "undefined" &&
                typeof params.location.latitude != "undefined" &&
                typeof params.location.longitude != "undefined") {
                var offset = (typeof params.offset == "object") ?
                    params.offset : new Microsoft.Maps.Point(0, 5);
                var text = (typeof params.text == "string") ?
                    params.text : "!";

                var pushpinOptions = {text : text,
                                      visible: true,
                                      textOffset: offset};
                var pushpin= new Microsoft.Maps.Pushpin(params.location, pushpinOptions);
                map.entities.push(pushpin);
            }
        };

        var addInfoBox = function( map, params ) {
            if (typeof params.location != "undefined" &&
                typeof params.location.latitude != "undefined" &&
                typeof params.location.longitude != "undefined") {
                var height = (typeof params.height != "undefined") ? params.height : 90;
                var width = (typeof params.width != "undefined") ? params.width : 130;
                var infoboxOptions = {
                    title           : params.title,
                    showPointer     : true,
                    showCloseButton : false,
                    height          : height,
                    width           : width
                };

                if (typeof params.description != "undefined") {
                    infoboxOptions.description = params.description;
                }

                if (typeof params.address != "undefined") {
                    var centerpoint = "cp=" + params.location.latitude + "~" + params.location.longitude ;
                    var url = "http://www.bing.com/maps/?v=2&" + centerpoint + "&lvl=10&style=r&where1=" + params.address;
                    var evtHandler = function() {
                        window.open (url,"rbaDirectionsWindow");
                    };

                    infoboxOptions.actions = [{label: 'Directions', eventHandler: evtHandler}];
                }

                var infobox = new Microsoft.Maps.Infobox(params.location, infoboxOptions );
                map.entities.push(infobox);
            }
        };

        var reKeyValues = ["^[ ]*(\\w+)[ ]*:[ ]*({[^{}]*}) *(?:$|;)",
                           "^[ ]*(\\w+)[ ]*:[ ]*([^;]*?)(?:$|;)" ];
        var re = [ new RegExp(reKeyValues[0]), new RegExp(reKeyValues[1])];
        var wsRegex = new RegExp("\\s+"); // whitespace

        var parseParamSpecifier = function(specifier) {
            if (-1 == specifier.indexOf(':')) {
                if (specifier.substring(0,1) == '"' &&
                    specifier.substring(specifier.length-1,specifier.length) == '"') {
                    return specifier.substring(1, specifier.length-1);
                }
                else {
                    return specifier;
                }
            }

            var parsedObject = {};
            var i;
            for(var s = specifier; s!== null; ) {
                // check for each regexp
                var found = false;
                for(i=0; i < re.length && !found; i++) {
                    var r1 = re[i].exec(s);
                    if (r1 !== null && (r1 instanceof Array) && r1.length == 3) {
                        found = true;
                        var value = null;
                        if ((i==1) && (r1[1] == "center" || r1[1] == "location"|| r1[1] == "pushpin")) {
                            var latlong = r1[2].split(wsRegex);
                            if (latlong instanceof Array && latlong.length == 2) {
                                value = new Microsoft.Maps.Location(latlong[0], latlong[1]);
                                if (r1[1]=="pushpin") {
                                    // embed location into an object, if this is a pushpin
                                    value = { location : value };
                                }
                            }
                        }
                        else if (r1[1] == "offset") {
                            var offset = r1[2].split(wsRegex);
                            if (offset instanceof Array && offset.length == 2) {
                                value = new Microsoft.Maps.Point(offset[0], offset[1]);
                            }
                        }
                        else if ((i==1) && (r1[1] == "height" || r1[1] == "width" || r1[1] == "zoom")) {
                            value = parseInt(r1[2],10);
                        }
                        else {
                            var v = r1[2].trim();
                            value = (i===0) ?
                                parseParamSpecifier(v.substring(1,v.length-1))
                                : parseParamSpecifier(v);
                        }
                        if (typeof parsedObject[r1[1]] == "undefined") {
                            parsedObject[r1[1]] = value ;
                        }
                        else if (parsedObject[r1[1]] instanceof Array){
                            parsedObject[r1[1]].push( value );
                        }
                        else {
                            // a prop by that name already exists. Convert to an array.
                            var firstValue = parsedObject[r1[1]];
                            parsedObject[r1[1]] = [ firstValue, value ] ;
                        }

                        // advance to the next thing in the string
                        s = s.substring(r1[0].length);
                    }
                }
                // no match found, all done parsing
                if (!found) {s = null;}
            }
            return parsedObject;
        };

        var displayMap = function(theDiv) {
            var elt = (typeof theDiv == "string")?
                document.getElementById(theDiv) : theDiv;

            if (elt === null) {return;}

            // Get the parameters for this particular map from a custom attribute.
            // According to HTML5 the custom attribute must start with data- .
            var mapdata = elt.getAttribute("data-mapdata");

            // format of this content is:   key1:value1[;key2:value2...]
            //
            // keys can be one of:  center, zoom, infobox, pushpin
            //
            // values:
            //   center: 2 numbers, separated by a space, specifying latitude
            //        and longitude, in degrees. example:
            //        center: 37.654488 -77.62337
            //
            //   zoom: a number, zoom level. 10 is city-wide zoom, and is the
            //        default. 7 is state-wide zoom. 2 is global zoom.
            //
            //   infobox: a specifier surrouned by curly-braces, providing the
            //        parameters for an information box that gets superimposed onto
            //        the map. The supported parameters are:
            //
            //     location: 2 numbers, specifying latitude and longitude.
            //
            //     title: title text to display in the infobox
            //
            //     description: (optional) text within the infobox
            //
            //     address: (optional) will cause a hyperlink to a directions page
            //
            //     height: height of the infobox, default 90
            //
            //     width: width of the infobox, default 130
            //
            //   pushpin: a specifier surrouned by curly-braces, providing the
            //        parameters for a pushpin displayed on the map. The supported
            //        parameters are:
            //
            //     location: 2 numbers, specifying latitude and longitude.
            //
            //     text: text to display for the pushpin.  For best results use
            //        one character for each pin.
            //
            // You can have multiple infobox elements and multiple pushpins.
            //
            // It's ok to change the order of the items inside the infobox curly braces.
            //
            // example:
            //
            //      <div id='map1' class='map'
            //           data-mapdata='center: 37.654488 -77.62337; infobox: {title: "infobox title"; location: 37.608696 -77.494041; address: "5904 School Ave. Richmond, VA 23228"}'></div>
            //

            var params = parseParamSpecifier(mapdata);
            if (typeof params.center != "undefined") {

                var zoom = (typeof params.zoom != "undefined") ? params.zoom : 10;

                // short pump: 37.654488, -77.62337
                var mapOptions = {
                    credentials : bingMapsKey,
                    center      : params.center,
                    mapTypeId   : Microsoft.Maps.MapTypeId.road,
                    zoom        : zoom
                };
                var map = new Microsoft.Maps.Map(elt, mapOptions);

                // handle all infobox specifiers
                if (typeof params.infobox != "undefined") {
                    if (params.infobox instanceof Array){
                        for(i=0; i < params.infobox.length; i++) {
                            addInfoBox(map, params.infobox[i]);
                        }
                    }
                    else{
                        addInfoBox(map, params.infobox);
                    }
                }

                // handle all pushpin specifiers
                if (typeof params.pushpin != "undefined") {
                    if (params.pushpin instanceof Array){
                        for(i=0; i < params.pushpin.length; i++) {
                            if (typeof params.pushpin[i].text == "undefined") {
                                params.pushpin[i].text = "" + (i+1);
                            }
                            addPushpin(map, params.pushpin[i]);
                        }
                    }
                    else{
                        addPushpin(map, params.pushpin);
                    }
                }
            }

            //addInfoBox(map, { title : 'RBA West\nRockville', location: new Microsoft.Maps.Location(37.698233, -77.663426), address: '2318 Commerce Center Drive Rockville, VA 23146'} );

            // var contents =
            //     '<div id="infoboxText" style="background-color:White; font-family:Tahoma,Arial; font-size: 10pt; border: DarkGrey 2px solid; min-height:80px; padding: 2px 2px 2px 2px; '+
            //     'position:absolute;top:-140px; left:15px; width:140px;">' +
            //     '<b id="infoboxTitle" style="margin:2px 2px 2px 2px;">RBA West</b>'+
            //     '<p style="margin:2px 2px 2px 2px;">5904 School Ave.<br/>Richmond, VA 23228</p>'+
            //     '</div>';
            // infobox.setHtmlContent(contents);
        };

        // function createDirectionsManager() {
        //     var displayMessage = "";
        //     if (directionsManager===null) {
        //         directionsManager = new Microsoft.Maps.Directions.DirectionsManager(map);
        //         displayMessage = 'Directions Module loaded<BR>';
        //         displayMessage += 'Directions Manager loaded';
        //     }
        //     displayAlert(displayMessage);
        //     directionsManager.resetDirections();
        //     directionsErrorEventObj = Microsoft.Maps.Events.addHandler(directionsManager, 'directionsError', function(arg) { alert(arg.message) });
        //     directionsUpdatedEventObj = Microsoft.Maps.Events.addHandler(directionsManager, 'directionsUpdated', function() { displayAlert('Directions updated') });
        // }

        // function directions() {
        //     if (!directionsManager) {
        //         Microsoft.Maps.loadModule('Microsoft.Maps.Directions', { callback: createDirectionsManager });
        //     }
        //     else {
        //         createDirectionsManager();
        //     }
        // }

        // put the bingMap object into global scope:
        bingMap = {
            displayMap : displayMap
        };
    }
})();
