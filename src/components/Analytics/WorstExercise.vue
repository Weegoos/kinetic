<template>
  <div>
    <q-card class="worstExercisesCard">
      <div id="worstExercises"></div>
    </q-card>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount } from "vue";
import * as echarts from "echarts";

onMounted(() => {
  const dom = document.getElementById("worstExercises");
  const myChart = echarts.init(dom, null, {
    renderer: "canvas",
    useDirtyRect: false,
  });

  const labelRight = {
    position: "right",
  };

  const option = {
    title: {
      text: "Худшие упражнение",
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
      data: ["Бег 3км", "Бег 100м", "Стрельба с винтовки"],
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
          { offset: 0, color: "#FFBF1A" }, // Start color
          { offset: 1, color: "#FF4080" }, // End color
        ]),
        data: [{ value: 5 }, { value: 8 }, { value: 7 }],
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
#worstExercises {
  position: relative;
  height: 300px;
  overflow: hidden;
  border-radius: 10px; /* Border radius for the chart container */
}

.worstExercisesCard {
  padding: 12px;
  border-radius: 10px;
}
</style>
