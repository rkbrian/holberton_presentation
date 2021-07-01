




    (function(){
        load(); // load the default or selected maze size
        $("#mySelect").combobox({
            onChange:load
        });
    });
    function load(){
        // use getvalue to acquire selected key (maze level)
        var lvl = $("#mySelect").combobox("getValue");
        if(lvl=="Medium"){
            width = 500;
            height = 300;
        } else if(lvl=="Hard") {
            width = 600;
            height = 400;
        } else if(lvl=="Expert") {
            width = 800;
            height = 600;
        } else {
            width = 400;
            height = 250;
        }
    }