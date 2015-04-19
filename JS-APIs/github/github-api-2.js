// JavaScript for github-api.html (GitHub git API)

var repoHTML = "<input type='text' name='user' value='jgbarah' " +
    "id='user' size='10' />" +
    "<input type='text' name='repo' value='GitHub-API' " +
    "id='repo' size='10' />" +
    "<button type='button'>Grab repo data</button>" +
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
    myrepo.write('master', 'data.json', "Holita", "First", function(err) {
	console.log (err)
    });
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
		      "</ul><div id='jsondata' />")
	console.log (repo.full_name, repo.description, repo.created_at);

	var repojson = {"fullname": repo.full_name,
			"description": repo.description,
			"created_at": repo.created_at
		       };
//	repository.write('master', 'data.json', JSON.stringify (repojson),
//			 'Repository data' + Date().toLocaleString(), 
//			 function(err) {
//			     console.log(err);
//			     ("#jsondata").html(err);
//			 });
//	myrepo.write('master', 'data.json', "Hola", "First", function(err) {});
    }
};

$(document).ready(function() {
    $("div#form button").click(getToken);
    
});
