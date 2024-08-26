<template>
  <div>
    <section class="col q-mb-md">
      <div class="row q-gutter-md">
        <div class="col">
          <q-card class="generalAnalytics">
            <p class="headline">Всего пройдено</p>
            <p>
              <span class="currentNumber">27</span>/<span class="generalNumber"
                >80</span
              >
            </p>
          </q-card>
        </div>
        <div class="col">
          <q-card class="generalAnalytics">
            <p class="headline">Всего пользователей</p>
            <p class="currentNumber">3.248</p>
          </q-card>
        </div>
        <div class="col">
          <q-card class="generalAnalytics">
            <p class="headline">Общее время</p>
            <p class="currentNumber">2м 34с</p>
          </q-card>
        </div>
      </div>
    </section>
    <section class="col">
      <div class="row q-gutter-md">
        <div class="col">
          <q-card class="generalAnalytics">
            <p class="headline">Начальные результаты</p>
            <p class="currentNumber">64%</p>
            <img src="../../assets/analytics/Graph.png" alt="" />
          </q-card>
        </div>
        <div class="col">
          <q-card class="generalAnalytics">
            <p class="headline">Текущие результаты</p>
            <p class="currentNumber">86%</p>
            <img src="../../assets/analytics/Graph.png" alt="" />
          </q-card>
        </div>
        <div class="col">
          <q-card class="generalAnalytics">
            <p class="headline">Прогресс</p>
            <p class="currentNumber">32%</p>
            <img src="../../assets/analytics/Graph.png" alt="" />
          </q-card>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.generalAnalytics {
  padding: 12px;
  border-radius: 10px;
}

.headline {
  /* font-size: 16px; */
}

.currentNumber {
  font-size: 25px;
  font-weight: bold;
}

.generalNumber {
  color: #898181;
}
</style>
