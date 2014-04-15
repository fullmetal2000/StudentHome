angular.module('sth.page1',['webix'])
  .controller('Page1Ctrl', function ($scope) {
  	$scope.text = "this is page1";
  	 $scope.lines = [
    //chart dataset
    { id:1, sales:20, year:"02"},
    { id:2, sales:55, year:"03"}
  ];
 
  $scope.changeLine = function(type){
    //methods are applied to the chart by its ID
    $$("mychart").define("type", type); 
    $$("mychart").render();
  };
  });
