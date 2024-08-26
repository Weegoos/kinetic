<template>
  <div>
    <div class="row q-gutter-md">
      <section class="col">
        <q-card class="my-card">
          <div ref="chartContainer" class="lineChart"></div>
        </q-card>
      </section>
      <section class="col">
        <q-card class="my-card">
          <div ref="barChart" class="lineChart"></div>
        </q-card>
      </section>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import * as echarts from "echarts/core";
import { LineChart, BarChart } from "echarts/charts";
import {
  TooltipComponent,
  LegendComponent,
  GridComponent,
  AxisPointerComponent,
} from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";

// Регистрируем необходимые компоненты
echarts.use([
  BarChart,
  LineChart,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  AxisPointerComponent,
  CanvasRenderer,
]);

const chartContainer = ref(null);
const barChart = ref("");
onMounted(() => {
  createLineChartForPhysicalResults();
  createBarChart();
});

const createLineChartForPhysicalResults = () => {
  const dom = chartContainer.value;
  const myChart = echarts.init(dom);

  const colors = ["#5470C6", "#EE6666"];

  const option = {
    color: colors,
    title: {
      text: "Физические результаты",
      left: "center",
      top: 20,
      textStyle: {
        fontSize: 20,
        fontWeight: "bold",
        color: "#333",
      },
    },
    tooltip: {
      trigger: "none",
      axisPointer: {
        type: "cross",
      },
    },
    legend: {},
    grid: {
      top: 70,
      bottom: 50,
    },
    xAxis: [
      {
        type: "category",
        axisTick: {
          alignWithLabel: true,
        },
        axisLine: {
          onZero: false,
          lineStyle: {
            color: colors[1],
          },
        },
        axisPointer: {
          label: {
            formatter: function (params) {
              return (
                "Осадок  " +
                params.value +
                (params.seriesData.length
                  ? "：" + params.seriesData[0].data
                  : "")
              );
            },
          },
        },
        // prettier-ignore
        data: ['2016-1', '2016-2', '2016-3', '2016-4', '2016-5', '2016-6', '2016-7', '2016-8', '2016-9', '2016-10', '2016-11', '2016-12'],
      },
      {
        type: "category",
        axisTick: {
          alignWithLabel: true,
        },
        axisLine: {
          onZero: false,
          lineStyle: {
            color: colors[0],
          },
        },
        axisPointer: {
          label: {
            formatter: function (params) {
              return (
                "Осадок  " +
                params.value +
                (params.seriesData.length
                  ? "：" + params.seriesData[0].data
                  : "")
              );
            },
          },
        },
        data: [
          "2015-1",
          "2015-2",
          "2015-3",
          "2015-4",
          "2015-5",
          "2015-6",
          "2015-7",
          "2015-8",
          "2015-9",
          "2015-10",
          "2015-11",
          "2015-12",
        ],
      },
    ],
    yAxis: [
      {
        type: "value",
      },
    ],
    series: [
      {
        name: "Отжимание",
        type: "line",
        xAxisIndex: 1,
        smooth: true,
        emphasis: {
          focus: "series",
        },
        data: [
          2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3,
        ],
      },
      {
        name: "Подтягивание",
        type: "line",
        smooth: true,
        emphasis: {
          focus: "series",
        },
        data: [
          3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7,
        ],
      },
    ],
  };

  myChart.setOption(option);

  window.addEventListener("resize", () => {
    myChart.resize();
  });
};

const createBarChart = () => {
  const dom = barChart.value;
  const myChart = echarts.init(dom);

  const option = {
    title: {
      text: "Изменение результатов",
      left: "center",
      top: 20,
      textStyle: {
        fontSize: 20,
        fontWeight: "bold",
        color: "#333",
      },
    },
    xAxis: {
      type: "category",
      data: ["Пн", "Вт", "Ср", "Чт", "Пт", "Суб", "Вск"],
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        data: [120, 200, 150, 80, 70, 110, 130],
        type: "bar",
      },
    ],
  };

  myChart.setOption(option);

  window.addEventListener("resize", () => {
    myChart.resize();
  });
};
</script>

<style scoped>
.lineChart {
  height: 250px;
  width: 100%;
}
</style>
