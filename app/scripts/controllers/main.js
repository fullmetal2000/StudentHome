'use strict';

angular.module('sth.home',['webix','ui.bootstrap'])
  .controller('MainCtrl', function ($scope) {
  	console.log('this is home')
	 $scope.tabs = [
	    { title:"Dynamic Title 1", content:"Dynamic content 1" },
	    { title:"Dynamic Title 2", content:"Dynamic content 2", disabled: true }
	  ];

	  $scope.alertMe = function() {
	    setTimeout(function() {
	      alert("You've selected the alert tab!");
	    });
	  };

  });
