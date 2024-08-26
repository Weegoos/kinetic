<template>
  <div class="q-ma-md">
    <section>
      <FilterGreeting />
    </section>
    <section class="q-mt-lg">
      <GeneralStatistics />
    </section>
    <section class="q-mt-lg">
      <ProgressChart />
    </section>
  </div>
</template>

<script setup>
import FilterGreeting from "../components/Result/FilterGreeting.vue";
import GeneralStatistics from "../components/Result/GeneralStatistics.vue";
import ProgressChart from "../components/Result/ProgressChart.vue";
</script>

<style></style>
