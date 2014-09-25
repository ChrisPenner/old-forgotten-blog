$(document).ready(function(){
    if (getCookie('theme')=='night') {
        switchTheme();
    }
    $('#theme-button').click(switchTheme);
});
function switchTheme(){
    var $button = $('#theme-button');
    $('html').toggleClass("dark");
    if($button.text() == "DAY"){
        $button.text("NIGHT");
        setCookie("theme", "night", 2*24*60*60*1000); //Expire in two days
    } else {
        $button.text("DAY");
        setCookie("theme", "day", 2*24*60*60*1000); //Expire in two days
    }
}

function setCookie(cname,cvalue,extime)
{
    var d = new Date();
    d.setTime(d.getTime()+(extime));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";" + "path=/"; 
}

function getCookie(cname)
{
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++)
    {
        var c = ca[i].trim();
        if (c.indexOf(name)===0) return c.substring(name.length,c.length);
    }
    return "";
}
