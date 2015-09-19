

$(function(){
	$('#searchButton').click(function(){
		searchTermFunction();
	});
	$('#search').keydown(function(event){
		
		if ( event.which == 13 ) {
			event.preventDefault();	
			 searchTermFunction();
		 }
	});
	$("#result").on("click",".article",function(){		
		$(".article").css("display","none");
		$(this).css("display","block");
		saveImageFunction($(this).find(".title").html(),$(this).find(".summary").find("img").attr("src"));
	});
	changeColor();
});
function saveImageFunction(title,image_url){
		var searchTerm = $('#searchTerm').val();
		var url = "/search/save/";	
		var image_url = image_url;
		
		$.ajax({
			url :url, 
            type : "POST",
            data:{"title":title,"image_url":image_url,"searchTerm":searchTerm},            
            dataType: "json",            
            success : function(data) {   
            	
            	$("#result").html(data['result']);
            	changeColor();
            	$("#success").text("<h2>Image is saved</h2>").delay(100).text(""); 
            	
            },			
		});
}

function searchTermFunction(){
	var searchTerm = $('#search').val();
	if (searchTerm.length>0) 
		{
		var url = "/search/"+"?searchTerm="+searchTerm;		
		$.ajax({
			url :url, 
            type : "GET",
            dataType: "json",            
            success : function(data) {   
            	
            	$("#result").html(data['result']);
            	changeColor();
            },			
		});
	}
	
}

function changeColor(){
	var colors = ["green","blue","light-green","orange","yellow","mehendi","purple"]
	var i=0;
	$(".article").each(function(){
		$(this).addClass(colors[i]);
		i = i+1;
		if(i>=colors.length){
			i=0;
		}		
	});
	$(".storeImages").each(function(){
		$(this).addClass(colors[i]);
		i = i+1;
		if(i>=colors.length){
			i=0;
		}		
	});
	var searchTerm = $('#searchTerm').val();
	$('#search').val(searchTerm);
	localStorage.setItem("searchTerm", searchTerm);
	var $container = $('#articles');
	// initialize
	$container.masonry({
	  columnWidth: 150,
	  itemSelector: '.article'
	});
	
	var $imageContainer = $('#storeImages');
	$imageContainer.masonry({
		  columnWidth: 150,
		  itemSelector: '.storeImages'
		});
	
}

