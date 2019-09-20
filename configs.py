<!DOCTYPE html>
<html class="" lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="sub3/configs.py · master · SSAFY 관리자 / ai-base" property="og:title">
<meta content="SSAFY 전용 GitLab 시스템" property="og:description">
<meta content="https://lab.ssafy.com/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://lab.ssafy.com/ssafyadmin/ai-base/blob/master/sub3/configs.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="sub3/configs.py · master · SSAFY 관리자 / ai-base" property="twitter:title">
<meta content="SSAFY 전용 GitLab 시스템" property="twitter:description">
<meta content="https://lab.ssafy.com/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="twitter:image">

<title>sub3/configs.py · master · SSAFY 관리자 / ai-base · GitLab</title>
<meta content="SSAFY 전용 GitLab 시스템" name="description">
<link rel="shortcut icon" type="image/png" href="/uploads/-/system/appearance/favicon/1/favicon.ico" id="favicon" data-original-href="/uploads/-/system/appearance/favicon/1/favicon.ico" />
<link rel="stylesheet" media="all" href="/assets/application-2832ca66c41eaf7e8aa1c5cbad98c671e92407d4fc0b6cbd545c48abfc707278.css" />
<link rel="stylesheet" media="print" href="/assets/print-c8ff536271f8974b8a9a5f75c0ca25d2b8c1dceb4cff3c01d1603862a0bdcbfc.css" />



<script>
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https://lab.ssafy.com/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=10;gon.asset_host=null;gon.webpack_public_path="/assets/webpack/";gon.relative_url_root="";gon.shortcuts_path="/help/shortcuts";gon.user_color_scheme="white";gon.gitlab_url="https://lab.ssafy.com";gon.revision="4d0c547e7d3";gon.gitlab_logo="/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png";gon.sprite_icons="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg";gon.sprite_file_icons="/assets/file_icons-7262fc6897e02f1ceaf8de43dc33afa5e4f9a2067f4f68ef77dcc87946575e9e.svg";gon.emoji_sprites_css_path="/assets/emoji_sprites-289eccffb1183c188b630297431be837765d9ff4aed6130cf738586fb307c170.css";gon.test_env=false;gon.suggested_label_colors=["#0033CC","#428BCA","#44AD8E","#A8D695","#5CB85C","#69D100","#004E00","#34495E","#7F8C8D","#A295D6","#5843AD","#8E44AD","#FFECDB","#AD4363","#D10069","#CC0033","#FF0000","#D9534F","#D1D100","#F0AD4E","#AD8D43"];gon.current_user_id=34;gon.current_username="zzangkkmin";gon.current_user_fullname="강민";gon.current_user_avatar_url="/uploads/-/system/user/avatar/34/avatar.png";
//]]>
</script>


<script src="/assets/webpack/runtime.c88e47f9.bundle.js" defer="defer"></script>
<script src="/assets/webpack/main.d5428fd9.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons~pages.groups~pages.groups.activity~pages.groups.boards~pages.groups.clusters.destroy~pages.g~90c6efc5.e5d74880.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons~pages.groups.milestones.edit~pages.groups.milestones.new~pages.projects.blame.show~pages.pro~e382f304.7541165b.chunk.js" defer="defer"></script>
<script src="/assets/webpack/pages.projects.blob.show.a2b55406.chunk.js" defer="defer"></script>
<script>
  window.uploads_path = "/ssafyadmin/ai-base/uploads";
</script>

<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="yNMrBPImXBW11Qh1NLqOjnAZNiptPptx7iw6KsOjqIY6MG+TdsV+r9lJJqNL3iGJiOLJX+1+HN50s2IthVFFlA==" />
<meta content="origin-when-cross-origin" name="referrer">
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#474D57" name="theme-color">
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-5a9cee0e8a51212e70b90c87c12f382c428870c0ff67d1eb034d884b78d2dae7.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-a6eec6aeb9da138e507593b464fdac213047e49d3093fc30e90d9a995df83ba3.png" sizes="76x76" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-retina-72e2aadf86513a56e050e7f0f2355deaa19cc17ed97bbe5147847f2748e5a3e3.png" sizes="120x120" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-retina-8ebe416f5313483d9c1bc772b5bbe03ecad52a54eba443e5215a22caed2a16a2.png" sizes="152x152" />
<link color="rgb(226, 67, 41)" href="/assets/logo-d36b5212042cebc89b96df4bf6ac24e43db316143e89926c0db839ff694d2de4.svg" rel="mask-icon">
<meta content="/assets/msapplication-tile-1196ec67452f618d39cdd85e2e3a542f76574c071051ae7effbfde01710eb17d.png" name="msapplication-TileImage">
<meta content="#30353E" name="msapplication-TileColor">



</head>

<body class="ui-indigo " data-find-file="/ssafyadmin/ai-base/find_file/master" data-group="" data-page="projects:blob:show" data-project="ai-base">


<header class="navbar navbar-gitlab qa-navbar navbar-expand-sm js-navbar">
<a class="sr-only gl-accessibility" href="#content-body" tabindex="1">Skip to content</a>
<div class="container-fluid">
<div class="header-content">
<div class="title-container">
<h1 class="title">
<a title="Dashboard" id="logo" href="/"><img data-src="/uploads/-/system/appearance/header_logo/1/ssafy_logo.png" class="lazy" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />
</a></h1>
<ul class="list-unstyled navbar-sub-nav">
<li id="nav-projects-dropdown" class="home dropdown header-projects qa-projects-dropdown"><button data-toggle="dropdown" type="button">
Projects
<svg class="caret-down"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#angle-down"></use></svg>
</button>
<div class="dropdown-menu frequent-items-dropdown-menu">
<div class="frequent-items-dropdown-container">
<div class="frequent-items-dropdown-sidebar qa-projects-dropdown-sidebar">
<ul>
<li class=""><a class="qa-your-projects-link" href="/dashboard/projects">Your projects
</a></li><li class=""><a href="/dashboard/projects/starred">Starred projects
</a></li><li class=""><a href="/explore">Explore projects
</a></li></ul>
</div>
<div class="frequent-items-dropdown-content">
<div data-project-id="5513" data-project-name="ai-base" data-project-namespace="SSAFY 관리자 / ai-base" data-project-web-url="/ssafyadmin/ai-base" data-user-name="zzangkkmin" id="js-projects-dropdown"></div>
</div>
</div>

</div>
</li><li id="nav-groups-dropdown" class="home dropdown header-groups qa-groups-dropdown"><button data-toggle="dropdown" type="button">
Groups
<svg class="caret-down"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#angle-down"></use></svg>
</button>
<div class="dropdown-menu frequent-items-dropdown-menu">
<div class="frequent-items-dropdown-container">
<div class="frequent-items-dropdown-sidebar qa-groups-dropdown-sidebar">
<ul>
<li class=""><a class="qa-your-groups-link" href="/dashboard/groups">Your groups
</a></li><li class=""><a href="/explore/groups">Explore groups
</a></li></ul>
</div>
<div class="frequent-items-dropdown-content">
<div data-user-name="zzangkkmin" id="js-groups-dropdown"></div>
</div>
</div>

</div>
</li><li class="d-none d-xl-block d-lg-block"><a class="dashboard-shortcuts-activity" title="Activity" href="/dashboard/activity">Activity
</a></li><li class="d-none d-xl-block d-lg-block"><a class="dashboard-shortcuts-milestones" title="Milestones" href="/dashboard/milestones">Milestones
</a></li><li class="d-none d-xl-block d-lg-block"><a class="dashboard-shortcuts-snippets" title="Snippets" href="/dashboard/snippets">Snippets
</a></li><li class="d-lg-none d-xl-none dropdown header-more">
<a data-toggle="dropdown" href="#">
More
<svg class="caret-down"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#angle-down"></use></svg>
</a>
<div class="dropdown-menu">
<ul>
<li class=""><a title="Activity" href="/dashboard/activity">Activity
</a></li><li class=""><a class="dashboard-shortcuts-milestones" title="Milestones" href="/dashboard/milestones">Milestones
</a></li><li class=""><a class="dashboard-shortcuts-snippets" title="Snippets" href="/dashboard/snippets">Snippets
</a></li>
</ul>
</div>
</li>
<li class="hidden">
<a title="Projects" class="dashboard-shortcuts-projects" href="/dashboard/projects">Projects
</a></li>

</ul>

</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li class="header-new dropdown">
<a class="header-new-dropdown-toggle has-tooltip qa-new-menu-toggle" title="New..." ref="tooltip" aria-label="New..." data-toggle="dropdown" data-placement="bottom" data-container="body" data-display="static" href="/projects/new"><svg class="s16"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#plus-square"></use></svg>
<svg class="caret-down"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#angle-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="dropdown-bold-header">
This project
</li>
<li><a href="/ssafyadmin/ai-base/issues/new">New issue</a></li>
<li><a href="/ssafyadmin/ai-base/snippets/new">New snippet</a></li>
<li class="divider"></li>
<li class="dropdown-bold-header">GitLab</li>
<li><a class="qa-global-new-project-link" href="/projects/new">New project</a></li>
<li><a href="/groups/new">New group</a></li>
<li><a href="/snippets/new">New snippet</a></li>
</ul>
</div>
</li>

<li class="nav-item d-none d-sm-none d-md-block m-auto">
<div class="search search-form">
<form class="form-inline" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><div class="search-input-container">
<div class="search-input-wrap">
<div class="dropdown" data-url="/search/autocomplete">
<input type="search" name="search" id="search" placeholder="Search or jump to…" class="search-input dropdown-menu-toggle no-outline js-search-dashboard-options" spellcheck="false" tabindex="1" autocomplete="off" data-issues-path="/dashboard/issues" data-mr-path="/dashboard/merge_requests" aria-label="Search or jump to…" />
<button class="hidden js-dropdown-search-toggle" data-toggle="dropdown" type="button"></button>
<div class="dropdown-menu dropdown-select">
<div class="dropdown-content"><ul>
<li class="dropdown-menu-empty-item">
<a>
Loading...
</a>
</li>
</ul>
</div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
<svg class="s16 search-icon"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#search"></use></svg>
<svg class="s16 clear-icon js-clear-input"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#close"></use></svg>
</div>
</div>
</div>
<input type="hidden" name="group_id" id="group_id" class="js-search-group-options" />
<input type="hidden" name="project_id" id="search_project_id" value="5513" class="js-search-project-options" data-project-path="ai-base" data-name="ai-base" data-issues-path="/ssafyadmin/ai-base/issues" data-mr-path="/ssafyadmin/ai-base/merge_requests" data-issues-disabled="false" />
<input type="hidden" name="search_code" id="search_code" value="true" />
<input type="hidden" name="repository_ref" id="repository_ref" value="master" />

<div class="search-autocomplete-opts hide" data-autocomplete-path="/search/autocomplete" data-autocomplete-project-id="5513" data-autocomplete-project-ref="master"></div>
</form></div>

</li>
<li class="nav-item d-inline-block d-sm-none d-md-none">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/search?project_id=5513"><svg class="s16"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#search"></use></svg>
</a></li>
<li class="user-counter"><a title="Issues" class="dashboard-shortcuts-issues" aria-label="Issues" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/issues?assignee_username=zzangkkmin"><svg class="s16"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#issues"></use></svg>
<span class="badge badge-pill hidden issues-count">
0
</span>
</a></li><li class="user-counter"><a title="Merge requests" class="dashboard-shortcuts-merge_requests" aria-label="Merge requests" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/merge_requests?assignee_username=zzangkkmin"><svg class="s16"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#git-merge"></use></svg>
<span class="badge badge-pill hidden merge-requests-count">
0
</span>
</a></li><li class="user-counter"><a title="Todos" aria-label="Todos" class="shortcuts-todos" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/todos"><svg class="s16"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#todo-done"></use></svg>
<span class="badge badge-pill hidden todos-count">
0
</span>
</a></li><li class="nav-item header-help dropdown">
<a class="header-help-dropdown-toggle" data-toggle="dropdown" href="/help"><svg class="s16"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#question"></use></svg>
<svg class="caret-down"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#angle-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li>
<a href="/help">Help</a>
</li>
<li>
<a target="_blank" class="text-nowrap" href="https://about.gitlab.com/contributing">Contribute to GitLab
</a></li>

</ul>

</div>
</li>
<li class="nav-item header-user dropdown">
<a class="header-user-dropdown-toggle" data-toggle="dropdown" href="/zzangkkmin"><img width="23" height="23" class="header-user-avatar qa-user-avatar lazy" data-src="/uploads/-/system/user/avatar/34/avatar.png?width=23" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />
<svg class="caret-down"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#angle-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="current-user">
<div class="user-name bold">
강민
</div>
@zzangkkmin
</li>
<li class="divider"></li>
<li>
<div class="js-set-status-modal-trigger" data-has-status="false"></div>
</li>
<li>
<a class="profile-link" data-user="zzangkkmin" href="/zzangkkmin">Profile</a>
</li>
<li>
<a href="/profile">Settings</a>
</li>
<li class="divider"></li>
<li>
<a class="sign-out-link" href="/users/sign_out">Sign out</a>
</li>
</ul>

</div>
</li>
</ul>
</div>
<button class="navbar-toggler d-block d-sm-none" type="button">
<span class="sr-only">Toggle navigation</span>
<svg class="s12 more-icon js-navbar-toggle-right"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#ellipsis_h"></use></svg>
<svg class="s12 close-icon js-navbar-toggle-left"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#close"></use></svg>
</button>
</div>
</div>
</header>
<div class="js-set-status-modal-wrapper" data-current-emoji="" data-current-message=""></div>

<div class="layout-page page-with-contextual-sidebar">
<div class="nav-sidebar">
<div class="nav-sidebar-inner-scroll">
<div class="context-header">
<a title="ai-base" href="/ssafyadmin/ai-base"><div class="avatar-container s40 project-avatar">
<div class="avatar s40 avatar-tile identicon bg5">A</div>
</div>
<div class="sidebar-context-title">
ai-base
</div>
</a></div>
<ul class="sidebar-top-level-items">
<li class="home"><a class="shortcuts-project" href="/ssafyadmin/ai-base"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#home"></use></svg>
</div>
<span class="nav-item-name">
Project
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/ssafyadmin/ai-base"><strong class="fly-out-top-item-name">
Project
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Project details" class="shortcuts-project" href="/ssafyadmin/ai-base"><span>Details</span>
</a></li><li class=""><a title="Activity" class="shortcuts-project-activity" href="/ssafyadmin/ai-base/activity"><span>Activity</span>
</a></li>
<li class=""><a title="Cycle Analytics" class="shortcuts-project-cycle-analytics" href="/ssafyadmin/ai-base/cycle_analytics"><span>Cycle Analytics</span>
</a></li></ul>
</li><li class="active"><a class="shortcuts-tree" href="/ssafyadmin/ai-base/tree/master"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#doc-text"></use></svg>
</div>
<span class="nav-item-name">
Repository
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><a href="/ssafyadmin/ai-base/tree/master"><strong class="fly-out-top-item-name">
Repository
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class="active"><a href="/ssafyadmin/ai-base/tree/master">Files
</a></li><li class=""><a href="/ssafyadmin/ai-base/commits/master">Commits
</a></li><li class=""><a href="/ssafyadmin/ai-base/branches">Branches
</a></li><li class=""><a href="/ssafyadmin/ai-base/tags">Tags
</a></li><li class=""><a href="/ssafyadmin/ai-base/graphs/master">Contributors
</a></li><li class=""><a href="/ssafyadmin/ai-base/network/master">Graph
</a></li><li class=""><a href="/ssafyadmin/ai-base/compare?from=master&amp;to=master">Compare
</a></li><li class=""><a href="/ssafyadmin/ai-base/graphs/master/charts">Charts
</a></li>
</ul>
</li><li class=""><a class="shortcuts-issues qa-issues-item" href="/ssafyadmin/ai-base/issues"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#issues"></use></svg>
</div>
<span class="nav-item-name">
Issues
</span>
<span class="badge badge-pill count issue_counter">
0
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/ssafyadmin/ai-base/issues"><strong class="fly-out-top-item-name">
Issues
</strong>
<span class="badge badge-pill count issue_counter fly-out-badge">
0
</span>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Issues" href="/ssafyadmin/ai-base/issues"><span>
List
</span>
</a></li><li class=""><a title="Board" href="/ssafyadmin/ai-base/boards"><span>
Board
</span>
</a></li><li class=""><a title="Labels" class="qa-labels-link" href="/ssafyadmin/ai-base/labels"><span>
Labels
</span>
</a></li>
<li class=""><a title="Milestones" class="qa-milestones-link" href="/ssafyadmin/ai-base/milestones"><span>
Milestones
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-merge_requests" href="/ssafyadmin/ai-base/merge_requests"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#git-merge"></use></svg>
</div>
<span class="nav-item-name">
Merge Requests
</span>
<span class="badge badge-pill count merge_counter js-merge-counter">
1
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/ssafyadmin/ai-base/merge_requests"><strong class="fly-out-top-item-name">
Merge Requests
</strong>
<span class="badge badge-pill count merge_counter js-merge-counter fly-out-badge">
1
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-pipelines qa-link-pipelines" href="/ssafyadmin/ai-base/pipelines"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#rocket"></use></svg>
</div>
<span class="nav-item-name">
CI / CD
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/ssafyadmin/ai-base/pipelines"><strong class="fly-out-top-item-name">
CI / CD
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Pipelines" class="shortcuts-pipelines" href="/ssafyadmin/ai-base/pipelines"><span>
Pipelines
</span>
</a></li><li class=""><a title="Jobs" class="shortcuts-builds" href="/ssafyadmin/ai-base/-/jobs"><span>
Jobs
</span>
</a></li><li class=""><a title="Schedules" class="shortcuts-builds" href="/ssafyadmin/ai-base/pipeline_schedules"><span>
Schedules
</span>
</a></li><li class=""><a title="Charts" class="shortcuts-pipelines-charts" href="/ssafyadmin/ai-base/pipelines/charts"><span>
Charts
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-operations" href="/ssafyadmin/ai-base/environments/metrics"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#cloud-gear"></use></svg>
</div>
<span class="nav-item-name">
Operations
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/ssafyadmin/ai-base/environments/metrics"><strong class="fly-out-top-item-name">
Operations
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Metrics" class="shortcuts-metrics" href="/ssafyadmin/ai-base/environments/metrics"><span>
Metrics
</span>
</a></li>
<li class=""><a title="Environments" class="shortcuts-environments qa-operations-environments-link" href="/ssafyadmin/ai-base/environments"><span>
Environments
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-wiki" href="/ssafyadmin/ai-base/wikis/home"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#book"></use></svg>
</div>
<span class="nav-item-name">
Wiki
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/ssafyadmin/ai-base/wikis/home"><strong class="fly-out-top-item-name">
Wiki
</strong>
</a></li></ul>
</li><li class=""><a class="shortcuts-snippets" href="/ssafyadmin/ai-base/snippets"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#snippet"></use></svg>
</div>
<span class="nav-item-name">
Snippets
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/ssafyadmin/ai-base/snippets"><strong class="fly-out-top-item-name">
Snippets
</strong>
</a></li></ul>
</li><li class=""><a title="Members" class="shortcuts-tree" href="/ssafyadmin/ai-base/settings/members"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#users"></use></svg>
</div>
<span class="nav-item-name">
Members
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/ssafyadmin/ai-base/project_members"><strong class="fly-out-top-item-name">
Members
</strong>
</a></li></ul>
</li><a class="toggle-sidebar-button js-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg class="icon-angle-double-left"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#angle-double-left"></use></svg>
<svg class="icon-angle-double-right"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#angle-double-right"></use></svg>
<span class="collapse-text">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg class="s16"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#close"></use></svg>
<span class="collapse-text">Close sidebar</span>
</button>
<li class="hidden">
<a title="Activity" class="shortcuts-project-activity" href="/ssafyadmin/ai-base/activity"><span>
Activity
</span>
</a></li>
<li class="hidden">
<a title="Network" class="shortcuts-network" href="/ssafyadmin/ai-base/network/master">Graph
</a></li>
<li class="hidden">
<a title="Charts" class="shortcuts-repository-charts" href="/ssafyadmin/ai-base/graphs/master/charts">Charts
</a></li>
<li class="hidden">
<a class="shortcuts-new-issue" href="/ssafyadmin/ai-base/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a title="Jobs" class="shortcuts-builds" href="/ssafyadmin/ai-base/-/jobs">Jobs
</a></li>
<li class="hidden">
<a title="Commits" class="shortcuts-commits" href="/ssafyadmin/ai-base/commits/master">Commits
</a></li>
<li class="hidden">
<a title="Issue Boards" class="shortcuts-issue-boards" href="/ssafyadmin/ai-base/boards">Issue Boards</a>
</li>
</ul>
</div>
</div>

<div class="content-wrapper">

<div class="mobile-overlay"></div>
<div class="alert-wrapper">




<nav class="breadcrumbs container-fluid container-limited" role="navigation">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav"><span class="sr-only">Open sidebar</span>
<i aria-hidden="true" data-hidden="true" class="fa fa-bars"></i>
</button><div class="breadcrumbs-links js-title-container">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a href="/ssafyadmin">SSAFY 연구팀</a><svg class="s8 breadcrumbs-list-angle"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#angle-right"></use></svg></li> <li><a href="/ssafyadmin/ai-base"><span class="breadcrumb-item-text js-breadcrumb-item-text">ai-base</span></a><svg class="s8 breadcrumbs-list-angle"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#angle-right"></use></svg></li>

<li>
<h2 class="breadcrumbs-sub-title"><a href="/ssafyadmin/ai-base/blob/master/sub3/configs.py">Repository</a></h2>
</li>
</ul>
</div>

</div>
</nav>

<div class="flash-container flash-container-page">
</div>

<div class="d-flex"></div>
</div>
<div class=" ">
<div class="content" id="content-body">
<div class="js-signature-container" data-signatures-path="/ssafyadmin/ai-base/commits/44ae8593e2c6636f50b62eecc2231ddb051689f2/signatures"></div>
<div class="container-fluid container-limited">

<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<form class="project-refs-form" action="/ssafyadmin/ai-base/refs/switch" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="destination" id="destination" value="blob" />
<input type="hidden" name="path" id="path" value="sub3/configs.py" />
<div class="dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown qa-branches-select" type="button" data-toggle="dropdown" data-selected="master" data-ref="master" data-refs-url="/ssafyadmin/ai-base/refs?sort=updated_desc" data-field-name="ref" data-submit-form-on-click="true" data-visit="true"><span class="dropdown-toggle-text ">master</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button>
<div class="dropdown-menu dropdown-menu-paging dropdown-menu-selectable git-revision-dropdown qa-branches-dropdown">
<div class="dropdown-page-one">
<div class="dropdown-title"><span>Switch branch/tag</span><button class="dropdown-title-button dropdown-menu-close" aria-label="Close" type="button"><i aria-hidden="true" data-hidden="true" class="fa fa-times dropdown-menu-close-icon"></i></button></div>
<div class="dropdown-input"><input type="search" id="" class="dropdown-input-field" placeholder="Search branches and tags" autocomplete="off" /><i aria-hidden="true" data-hidden="true" class="fa fa-search dropdown-input-search"></i><i aria-hidden="true" data-hidden="true" role="button" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/ssafyadmin/ai-base/tree/master">ai-base
</a></li>
<li class="breadcrumb-item">
<a href="/ssafyadmin/ai-base/tree/master/sub3">sub3</a>
</li>
<li class="breadcrumb-item">
<a href="/ssafyadmin/ai-base/blob/master/sub3/configs.py"><strong>configs.py</strong>
</a></li>
</ul>
</div>
<div class="tree-controls">
<a class="btn shortcuts-find-file" rel="nofollow" href="/ssafyadmin/ai-base/find_file/master"><i aria-hidden="true" data-hidden="true" class="fa fa-search"></i>
<span>Find file</span>
</a>
<div class="btn-group" role="group"><a class="btn js-blob-blame-link" href="/ssafyadmin/ai-base/blame/master/sub3/configs.py">Blame</a><a class="btn" href="/ssafyadmin/ai-base/commits/master/sub3/configs.py">History</a><a class="btn js-data-file-blob-permalink-url" href="/ssafyadmin/ai-base/blob/44ae8593e2c6636f50b62eecc2231ddb051689f2/sub3/configs.py">Permalink</a></div>
</div>
</div>

<div class="info-well d-none d-sm-block">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-44ae8593">
<div class="avatar-cell d-none d-sm-block">
<a href="/student1"><img alt="student1&#39;s avatar" src="https://secure.gravatar.com/avatar/3bfdf5862a4060969dffe4ce97372568?s=72&amp;d=identicon" class="avatar s36 d-none d-sm-inline" title="student1" /></a>
</div>
<div class="commit-detail flex-list">
<div class="commit-content qa-commit-content">
<a class="commit-row-message item-title" href="/ssafyadmin/ai-base/commit/44ae8593e2c6636f50b62eecc2231ddb051689f2">Update data.py</a>
<span class="commit-row-message d-block d-sm-none">
&middot;
44ae8593
</span>
<button class="text-expander js-toggle-button">
<svg class="s12"><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#ellipsis_h"></use></svg>
</button>
<div class="committer">
<a class="commit-author-link" href="/student1">student1</a> authored <time class="js-timeago" title="Sep 20, 2019 5:47pm" datetime="2019-09-20T08:47:25Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Sep 20, 2019</time>
</div>
<pre class="commit-row-description js-toggle-content append-bottom-8"> - sequence_index 오타 -&gt; seq_index&#x000A;&#x000A;Update configs.py&#x000A; - 누락된 파라미터에 대한 수정</pre>
</div>
<div class="commit-actions flex-row d-none d-sm-flex">

<div class="js-commit-pipeline-status" data-endpoint="/ssafyadmin/ai-base/commit/44ae8593e2c6636f50b62eecc2231ddb051689f2/pipelines?ref=master"></div>
<div class="commit-sha-group">
<div class="label label-monospace">
44ae8593
</div>
<button class="btn btn btn-default" data-toggle="tooltip" data-placement="bottom" data-container="body" data-title="Copy commit SHA to clipboard" data-class="btn btn-default" data-clipboard-text="44ae8593e2c6636f50b62eecc2231ddb051689f2" type="button" title="Copy commit SHA to clipboard" aria-label="Copy commit SHA to clipboard"><svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#duplicate"></use></svg></button>

</div>
</div>
</div>
</li>

</ul>
</div>


</div>
<div class="blob-content-holder" id="blob-content-holder">
<article class="file-holder">
<div class="js-file-title file-title-flex-parent">
<div class="file-header-content">
<i aria-hidden="true" data-hidden="true" class="fa fa-file-text-o fa-fw"></i>
<strong class="file-title-name">
configs.py
</strong>
<button class="btn btn-clipboard btn-transparent prepend-left-5" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn-clipboard btn-transparent prepend-left-5" data-title="Copy file path to clipboard" data-clipboard-text="{&quot;text&quot;:&quot;sub3/configs.py&quot;,&quot;gfm&quot;:&quot;`sub3/configs.py`&quot;}" type="button" title="Copy file path to clipboard" aria-label="Copy file path to clipboard"><svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#duplicate"></use></svg></button>
<small>
1.52 KB
</small>
</div>

<div class="file-actions">

<div class="btn-group" role="group"><button class="btn btn btn-sm js-copy-blob-source-btn" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn btn-sm js-copy-blob-source-btn" data-title="Copy source to clipboard" data-clipboard-target=".blob-content[data-blob-id=&#39;bdb7d153fc52e9151aee776718a699f0b7779418&#39;]" type="button" title="Copy source to clipboard" aria-label="Copy source to clipboard"><svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#duplicate"></use></svg></button><a class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" title="Open raw" data-container="body" href="/ssafyadmin/ai-base/raw/master/sub3/configs.py"><i aria-hidden="true" data-hidden="true" class="fa fa-file-code-o"></i></a><a download="sub3/configs.py" class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" title="Download" data-container="body" href="/ssafyadmin/ai-base/raw/master/sub3/configs.py?inline=false"><svg><use xlink:href="/assets/icons-1bbf3f0e2e8f631ea6006c647f843db214684476054223102c16630dabc450d4.svg#download"></use></svg></a></div>
<div class="btn-group" role="group"><button name="button" type="submit" class="btn js-edit-blob  js-edit-blob-link-fork-toggler" data-action="edit" data-fork-path="/ssafyadmin/ai-base/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2Fssafyadmin%2Fai-base%2Fedit%2Fmaster%2Fsub3%2Fconfigs.py&amp;namespace_key=34">Edit</button><button name="button" type="submit" class="btn btn-default js-edit-blob-link-fork-toggler" data-action="edit" data-fork-path="/ssafyadmin/ai-base/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2F-%2Fide%2Fproject%2Fssafyadmin%2Fai-base%2Fedit%2Fmaster%2F-%2Fsub3%2Fconfigs.py&amp;namespace_key=34">Web IDE</button><button name="button" type="submit" class="btn btn-default js-edit-blob-link-fork-toggler" data-action="replace" data-fork-path="/ssafyadmin/ai-base/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.+Try+to+replace+this+file+again.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2Fssafyadmin%2Fai-base%2Fblob%2Fmaster%2Fsub3%2Fconfigs.py&amp;namespace_key=34">Replace</button><button name="button" type="submit" class="btn btn-remove js-edit-blob-link-fork-toggler" data-action="delete" data-fork-path="/ssafyadmin/ai-base/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.+Try+to+delete+this+file+again.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2Fssafyadmin%2Fai-base%2Fblob%2Fmaster%2Fsub3%2Fconfigs.py&amp;namespace_key=34">Delete</button></div>
</div>
</div>
<div class="js-file-fork-suggestion-section file-fork-suggestion hidden">
<span class="file-fork-suggestion-note">
You're not allowed to
<span class="js-file-fork-suggestion-section-action">
edit
</span>
files in this project directly. Please fork this project,
make your changes there, and submit a merge request.
</span>
<a class="js-fork-suggestion-button btn btn-grouped btn-inverted btn-success" rel="nofollow" data-method="post" href="/ssafyadmin/ai-base/blob/master/sub3/configs.py">Fork</a>
<button class="js-cancel-fork-suggestion-button btn btn-grouped" type="button">
Cancel
</button>
</div>



<div class="blob-viewer" data-type="simple" data-url="/ssafyadmin/ai-base/blob/master/sub3/configs.py?format=json&amp;viewer=simple">
<div class="text-center prepend-top-default append-bottom-default">
<i aria-hidden="true" aria-label="Loading content…" class="fa fa-spinner fa-spin fa-2x"></i>
</div>

</div>


</article>
</div>

<div class="modal" id="modal-upload-blob">
<div class="modal-dialog modal-lg">
<div class="modal-content">
<div class="modal-header">
<h3 class="page-title">Replace configs.py</h3>
<button aria-label="Close" class="close" data-dismiss="modal" type="button">
<span aria-hidden="true">&times;</span>
</button>
</div>
<div class="modal-body">
<form class="js-quick-submit js-upload-blob-form" data-method="put" action="/ssafyadmin/ai-base/update/master/sub3/configs.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="VpoUvVuA/JRxDUjWCP8dDbt5YA+glZyrJPSntGxhs6CkeVAq32PeLh2RZgB3m7IKQ4KfeiDVGwS+a/+zKpNesg==" /><div class="dropzone">
<div class="dropzone-previews blob-upload-dropzone-previews">
<p class="dz-message light">
Attach a file by drag &amp; drop or <a class="markdown-selector" href="#">click to upload</a>
</p>
</div>
</div>
<br>
<div class="dropzone-alerts alert alert-danger data" style="display:none"></div>
<div class="form-group row commit_message-group">
<label class="col-form-label col-sm-2" for="commit_message-8461769939ba405f213a873cbf5b3218">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-8461769939ba405f213a873cbf5b3218" class="form-control js-commit-message" placeholder="Replace configs.py" required="required" rows="3">
Replace configs.py</textarea>
</div>
</div>
</div>

<input type="hidden" name="branch_name" id="branch_name" />
<input type="hidden" name="create_merge_request" id="create_merge_request" value="1" />
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch" />

<div class="form-actions">
<button name="button" type="button" class="btn btn-success btn-upload-file" id="submit-all"><i aria-hidden="true" data-hidden="true" class="fa fa-spin fa-spinner js-loading-icon hidden"></i>
Replace file
</button><a class="btn btn-cancel" data-dismiss="modal" href="#">Cancel</a>
<div class="inline prepend-left-10">
A new branch will be created in your fork and a new merge request will be started.
</div>

</div>
</form></div>
</div>
</div>
</div>

</div>
</div>

</div>
</div>
</div>
</div>


</body>
</html>

