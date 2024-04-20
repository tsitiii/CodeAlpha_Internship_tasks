var tablinks=document.getElementsByClassName("tab-links");
        var tabcontents=document.getElementsByClassName("tab-contents");

        function opentab(tabname) {
            for (const tablink of tablinks) {
                tablink.classList.remove("active-links");
            }

            for (const tabcontent of tabcontents) {
                tabcontent.classList.remove("active-tab");
            }
            event.currentTarget.classList.add("active-links");
            document.getElementById(tabname).classList.add("active-tab");
        }


        function popup(){
        alert("your response has been recorded!");
        let data=document.getElementById("formm");
        data.preventDefault();
         }