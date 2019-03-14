var w = 250, h = 250;
d3.select(".graph")
	.append("svg")
	.attr("width", w)
	.attr("height", h)
	.attr("id", "graphWrap");
var graphWrap = d3.select("#graphWrap");

// 그래프 데이터 // 합쳐서 100이 아니더라도 원이 생성됨
var graphData = [15, 25, 60];
// pie 생성
// var pie = d3.layout.pie(); // d3 v3 버전
var pie = d3.pie();
// 안쪽 반지름, 바깥쪽 반지름 설정 // 200x200 의 원 그래프 생성
// var arc = d3.svg.arc().innerRadius(0).outerRadius(100); // d3 v3 버전
var arc = d3.arc().innerRadius(0).outerRadius(100);

// 원 그리기
var oneGraph = graphWrap.selectAll("path").data(pie(graphData));
// 데이터 추가
oneGraph.enter()
	.append("path")
	.attr("class", "pie") // 클래스 추가
	// .attr("d", arc) // 부채꼴 지정
	// .attr("stroke", "black")
	.attr("transform", "translate("+(w/2)+","+(h/2)+")")
	.style("fill", function(d, i) {
		return ["red", "orange", "yellow", "blue", "purple"][i];
	})
	.transition()
	.duration(1000)
	.delay(function(d, i) {
		return i * 1000;
	})
	.attrTween("d", function(d, i) {
		var interpolate = d3.interpolate(
			{startAngle : d.startAngle, endAngle : d.startAngle},
			{startAngle : d.startAngle, endAngle : d.endAngle}
		);
		return function(t){
			return arc(interpolate(t));
		}
	});
