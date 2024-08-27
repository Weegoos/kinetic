<template>
  <div>
    <q-card class="chart">
      <div class="row" style="align-items: stretch">
        <div class="col">
          <p class="text-bold text-h6">Деятельность</p>
        </div>
        <div class="col" align="right">
          <q-input dense v-model="time" type="text" label="Время" list="sort" />
          <datalist id="sort">
            <div v-for="(items, id) in timeOptions" :key="id">
              <option :value="items"></option>
            </div>
          </datalist>
        </div>
      </div>
      <br />
      <q-separator />
      <div id="chart-container"></div>
    </q-card>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref } from "vue";
import * as echarts from "echarts";

onMounted(() => {
  const dom = document.getElementById("chart-container");
  const myChart = echarts.init(dom, null, {
    renderer: "canvas",
    useDirtyRect: false,
  });

  const option = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow",
      },
    },
    grid: {
      left: "3%",
      right: "4%",
      bottom: "3%",
      containLabel: true,
    },
    xAxis: [
      {
        type: "category",
        data: ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вск"],
        axisTick: {
          alignWithLabel: true,
        },
      },
    ],
    yAxis: [
      {
        type: "value",
      },
    ],
    series: [
      {
        name: "Деятельность",
        type: "bar",
        barWidth: "60%",
        data: [10, 52, 200, 334, 390, 330, 220],
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

const time = ref('')
const timeOptions = ["День", "Неделя", "Месяц", "Год"];
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.chart {
  padding: 12px;
  border-radius: 10px;
}
#chart-container {
  position: relative;
  height: 250px;
  overflow: hidden;
}
</style>
