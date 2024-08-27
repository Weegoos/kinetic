<template>
  <div>
    <section class="row q-gutter-md">
      <div class="col">
        <q-card class="my-card row">
          <div class="col">
            <div ref="power" class="chart" @click="showResultOfExercises"></div>
            <p class="description" align="center">Сила</p>
          </div>
          <div class="col">
            <div
              ref="endurance"
              class="chart"
              @click="showResultOfExercises"
            ></div>
            <p class="description" align="center">Выносливость</p>
          </div>
          <div class="col">
            <div ref="speed" class="chart" @click="showResultOfExercises"></div>
            <p class="description" align="center">Скорость</p>
          </div>
        </q-card>
      </div>
    </section>
    <SpeedDialog
      :chartName="chartName"
      :exercisesDialog="exercisesDialog"
      @close="closeDialog"
    />
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import * as echarts from "echarts/core";
import { PieChart } from "echarts/charts";
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
import { useQuasar } from "quasar";
import SpeedDialog from "../PhysicalExerises/DialogPage.vue";
echarts.use([
  PieChart,
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
const chartName = ref("");

onMounted(() => {
  createChart(
    power.value,
    "Сила",
    "#FF5B5B",
    "#FFE4E4",
    5,
    95,
    () => (chartName.value = "Сила")
  );
  createChart(
    endurance.value,
    "Выносливость",
    "#00B074",
    "#DBF3EB",
    22,
    78,
    () => (chartName.value = "Выносливость")
  );
  createChart(
    speed.value,
    "Скорость",
    "#2D9CDB",
    "#B4DFF7",
    72,
    28,
    () => (chartName.value = "Скорость")
  );
});

const createChart = (
  item,
  itemName,
  mainColor,
  remainColor,
  mainValue,
  remainValue,
  onClickHandler
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
  myChart.on("click", onClickHandler);
  window.addEventListener("resize", () => {
    myChart.resize();
  });
};

const $q = useQuasar();
const exercisesDialog = ref(false);
const showResultOfExercises = () => {
  exercisesDialog.value = true;
};

const closeDialog = () => {
  exercisesDialog.value = false;
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
