// JavaScript for github-api.html (GitHub git API)

var repoHTML = "<input type='text' name='user' value='jgbarah' " +
    "id='user' size='10' />" +
    "<input type='text' name='repo' value='GitHub-API' " +
    "id='repo' size='10' />" +
    "<button id='repobutton' type='button'>Grab repo data</button>" +
    "<div id='repodata'/>";

var github;
var myrepo;

// function btoa(data) {
//    return window.btoa(data);
// };

function getToken() {
    var token = $("#token").val();
    console.log (token);

    github = new Github({
	token: token,
	auth: "oauth"
    });

    $("#repoform").html(repoHTML)
    $("div#form button").click(getRepo);
};

function getRepo() {
    var user = $("#user").val();
    var reponame = $("#repo").val();
    myrepo = github.getRepo(user, reponame);
    myrepo.show(showRepo);
};

function showRepo(error, repo) {
    var repodata = $("#repodata");
    if (error) {
	repodata.html("<p>Error code: " + error.error + "</p>");
    } else {
	repodata.html("<p>Repo data:</p>" +
		      "<ul><li>Full name: " + repo.full_name + "</li>" +
		      "<li>Description: " + repo.description + "</li>" +
		      "<li>Created at: " + repo.created_at + "</li>" +
		      "</ul>" +
		      "<div id='repocontents' />");
	console.log (repo.full_name, repo.description, repo.created_at);
	myrepo.contents('master', '', listFiles);
    }
};

function listFiles(error, contents) {
    var repocontents = $("#repocontents");
    if (error) {
	repocontents.html("<p>Error code: " + error.error + "</p>");
    } else {
	var files = [];
	for (var i = 0, len = contents.length; i < len; i++) {
	    files.push(contents[i].name);
	};
	repocontents.html("<p>Contents:</p>" +
			  "<ul><li>" + files.join("</li><li>") +
			  "</li></ul>" +
			  "<input type='text' name='filename' " +
			  "value='datafile' " +
			  "id='filename' size='20' />" +
			  "<input type='text' name='content' " +
			  "value='Some content' " +
			  "id='content' size='40' />" +
			  "<button type='button' id='write'>" +
			  "Write File!</button>" +
			  "<div id='writefile' />"
			 );
	$("#write").click(writeFile);
    };
}

function writeFile() {
    var filename = $("#filename").val();
    var content = $("#content").val();
//    myrepo.write('master', filename, content,
    myrepo.write('master', 'datafile', 
		 new Date().toLocaleString(),
		 "Updating data", function(err) {
		     console.log (err)
		 });
    $("#writefile").html("<button type='button' id='read'>" +
			 "Read File!</button>" +
			 "<div id='readfile' />");
    $("#read").click(readFile);
};

function readFile() {
    var filename = $("#file").val();
    myrepo.read('master', filename, function(err, data) {
	$("#readfile").html("<p>Contents:</p><p>" + data + "</p>");
    });
};

$(document).ready(function() {
    hello.init({
	github : "066ef56a5d1d7cf39a3a"
    },{
	redirect_uri : 'redirect.html',
	oauth_proxy : "https://auth-server.herokuapp.com/proxy",
	scope : "publish_files",
    });
    access = hello("github");
    access.login({response_type: 'code'}).then( function(){
	auth = hello("github").getAuthResponse();
	token = auth.access_token;
	console.log (token);
	github = new Github({
	    token: token,
	    auth: "oauth"
	});
	$("#repoform").html(repoHTML);
	$("#repobutton").click(getRepo);
    }, function( e ){
	alert('Signin error: ' + e.error.message);
    });
});
