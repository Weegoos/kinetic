<template>
  <div>
    <section class="row q-gutter-md">
      <div class="col">
        <q-card class="my-card row">
          <div class="col">
            <div ref="power" class="chart"></div>
            <p class="description" align="center">Сила</p>
          </div>
          <div class="col">
            <div ref="endurance" class="chart"></div>
            <p class="description" align="center">Выносливость</p>
          </div>
          <div class="col">
            <div ref="speed" class="chart"></div>
            <p class="description" align="center">Скорость</p>
          </div>
        </q-card>
      </div>
      <div class="col">
        <q-card class="my-card">
          <div ref="chartContainer" class="linearChart"></div>
        </q-card>
      </div>
    </section>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import * as echarts from "echarts/core";
import { PieChart, LineChart } from "echarts/charts";
import {
  TooltipComponent,
  ToolboxComponent,
  TitleComponent,
  DataZoomComponent,
  GridComponent,
  AxisPointerComponent,
  LegendComponent,
} from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";

echarts.use([
  PieChart,
  LineChart,
  TooltipComponent,
  ToolboxComponent,
  TitleComponent,
  DataZoomComponent,
  GridComponent,
  AxisPointerComponent,
  LegendComponent,
  CanvasRenderer,
]);

const power = ref(null);
const endurance = ref(null);
const speed = ref(null);
const chartContainer = ref(null);

onMounted(() => {
  createChart(power.value, "Сила", "#FF5B5B", "#FFE4E4", 5, 95);
  createChart(endurance.value, "Выносливость", "#00B074", "#DBF3EB", 22, 78);
  createChart(speed.value, "Скорость", "#2D9CDB", "#B4DFF7", 72, 28);
  createLinearChart();
});

const createChart = (
  item,
  itemName,
  mainColor,
  remainColor,
  mainValue,
  remainValue
) => {
  const myChart = echarts.init(item);

  const option = {
    tooltip: {
      trigger: "item",
    },
    legend: {
      show: false,
    },
    series: [
      {
        name: itemName,
        type: "pie",
        radius: ["50%", "70%"],
        avoidLabelOverlap: false,
        itemStyle: {
          color: mainColor,
        },
        label: {
          show: true,
          position: "center",
          formatter: "{d}%",
          fontSize: 40,
          fontWeight: "bold",
          color: "#4A4A4A",
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 40,
            fontWeight: "bold",
            color: "#4A4A4A",
          },
        },
        labelLine: {
          show: false,
        },
        data: [
          { value: mainValue, name: itemName },
          {
            value: remainValue,
            name: "Invisible",
            itemStyle: { color: remainColor },
            label: { show: false },
            tooltip: { show: false },
          },
        ],
      },
    ],
  };

  myChart.setOption(option);

  window.addEventListener("resize", () => {
    myChart.resize();
  });
};

const createLinearChart = () => {
  let base = +new Date(2020, 0, 1);
  let oneDay = 24 * 3600 * 1000;
  let data = [[base, Math.random() * 300]];
  for (let i = 1; i < 365 * 2; i++) {
    let now = new Date((base += oneDay));
    data.push([+now, Math.round((Math.random() - 0.5) * 20 + data[i - 1][1])]);
  }

  const lineChart = echarts.init(chartContainer.value);

  const option = {
    tooltip: {
      trigger: "axis",
      position: function (pt) {
        return [pt[0], "10%"];
      },
    },
    title: {
      left: "center",
      text: "Large Area Chart with Weekly Intervals",
    },
    toolbox: {
      feature: {
        dataZoom: {
          yAxisIndex: "none",
          title: "Масштабирование",
        },
        restore: {
          title: "Сброс",
        },
        saveAsImage: {
          title: "Сохранить как изображение",
        },
      },
    },
    xAxis: {
      type: "time",
      boundaryGap: false,
      axisLabel: {
        formatter: function (value) {
          let date = new Date(value);
          return `${date.getFullYear()}-${
            date.getMonth() + 1
          }-${date.getDate()}`;
        },
        interval: 1000 * 60 * 60 * 24 * 7, // Показать метки каждую неделю
      },
      axisPointer: {
        show: true,
        type: "line",
      },
    },
    yAxis: {
      type: "value",
      boundaryGap: [0, "100%"],
    },
    dataZoom: [
      {
        type: "inside",
        start: 0,
        end: 20,
      },
      {
        start: 0,
        end: 20,
      },
    ],
    series: [
      {
        name: "Данные",
        type: "line",
        smooth: true,
        symbol: "none",
        areaStyle: {},
        data: data,
      },
    ],
  };

  lineChart.setOption(option);

  window.addEventListener("resize", () => {
    lineChart.resize();
    [power.value, endurance.value, speed.value].forEach((chartEl) => {
      if (chartEl) echarts.getInstanceByDom(chartEl)?.resize();
    });
  });
};
</script>

<style scoped>
.description {
  color: #464255;
  font-size: 20px;
}

.chart {
  height: 210px;
}

.linearChart {
  height: 255px;
}
</style>
