<template>
  <div>
    <q-card class="bestExercisesCard">
      <div id="bestExercises"></div>
    </q-card>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount } from "vue";
import * as echarts from "echarts";

onMounted(() => {
  const dom = document.getElementById("bestExercises");
  const myChart = echarts.init(dom, null, {
    renderer: "canvas",
    useDirtyRect: false,
  });

  const labelRight = {
    position: "right",
  };

  const option = {
    title: {
      text: "Лучшие упражнение",
    },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow",
      },
      formatter: "{b}: {c}%", // Show percentage in tooltip
    },
    grid: {
      top: 80,
      bottom: 30,
    },
    xAxis: {
      type: "value",
      position: "top",
      splitLine: {
        lineStyle: {
          type: "dashed",
        },
      },
      axisLabel: {
        formatter: "{value}%",
      },
    },
    yAxis: {
      type: "category",
      axisLine: { show: false },
      axisLabel: { show: false },
      axisTick: { show: false },
      splitLine: { show: false },
      data: ["Отжимание", "Подтягивание", "Стрельба с лука"],
    },
    series: [
      {
        name: "Cost",
        type: "bar",
        stack: "Total",
        label: {
          show: true,
          formatter: "{b}",
          color: "#fff",
        },
        color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
          { offset: 0, color: "#2FEA9B" }, // Start color
          { offset: 1, color: "#7FDD53" }, // End color
        ]),
        data: [{ value: 95 }, { value: 75 }, { value: 70 }],
      },
    ],
  };

  if (option && typeof option === "object") {
    myChart.setOption(option);
  }

  window.addEventListener("resize", myChart.resize);

  onBeforeUnmount(() => {
    window.removeEventListener("resize", myChart.resize);
    myChart.dispose();
  });
});
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
#bestExercises {
  position: relative;
  height: 300px;
  overflow: hidden;
  border-radius: 10px; /* Border radius for the chart container */
}

.bestExercisesCard {
  padding: 12px;
  border-radius: 10px;
}
</style>
