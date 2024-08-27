<template>
  <div>
    <section class="row q-gutter-md">
      <q-card class="my-card col">
        <div class="row q-gutter-sm card-wrapper">
          <div class="col" align="right">
            <img
              src="../../assets/result/GeneralStatistics/GeneralExercises.png"
              alt=""
              class="icon"
            />
          </div>
          <div class="col-8">
            <span class="text_class" id="headline">75</span>
            <span class="text_class" id="description">Всего упражнений</span>
            <div class="row">
              <div class="col-1 q-mr-sm">
                <img
                  src="../../assets/result/GeneralStatistics/arrawUp.png"
                  alt=""
                />
              </div>
              <div class="col percentage">4% (30 дней)</div>
            </div>
          </div>
        </div>
      </q-card>
      <q-card class="my-card col">
        <div class="row q-gutter-sm card-wrapper">
          <div class="col" align="right">
            <img
              src="../../assets/result/GeneralStatistics/Amount.png"
              alt=""
              class="icon"
            />
          </div>
          <div class="col-8">
            <span class="text_class" id="headline">357</span>
            <span class="text_class" id="description">Всего повторений</span>
            <div class="row">
              <div class="col-1 q-mr-sm">
                <img
                  src="../../assets/result/GeneralStatistics/arrawUp.png"
                  alt=""
                />
              </div>
              <div class="col percentage">4% (30 дней)</div>
            </div>
          </div>
        </div>
      </q-card>
      <q-card class="my-card col">
        <div class="row q-gutter-sm card-wrapper">
          <div class="col" align="right">
            <img
              src="../../assets/result/GeneralStatistics/Completed.png"
              alt=""
              class="icon"
            />
          </div>
          <div class="col-8">
            <span class="text_class" id="headline">65</span>
            <span class="text_class" id="description">Всего пройдено</span>
            <div class="row">
              <div class="col-1 q-mr-sm">
                <img
                  src="../../assets/result/GeneralStatistics/arrow_down.png"
                  alt=""
                />
              </div>
              <div class="col percentage">4% (30 дней)</div>
            </div>
          </div>
        </div>
      </q-card>
      <q-card class="my-card col">
        <div class="row q-gutter-sm card-wrapper">
          <div class="col" align="right">
            <img
              src="../../assets/result/GeneralStatistics/Points.png"
              alt=""
              class="icon"
            />
          </div>
          <div class="col-8">
            <span class="text_class" id="headline">185</span>
            <span class="text_class" id="description">Всего баллов</span>
            <div class="row">
              <div class="col-1 q-mr-sm">
                <img
                  src="../../assets/result/GeneralStatistics/arrow_down.png"
                  alt=""
                />
              </div>
              <div class="col percentage">4% (30 дней)</div>
            </div>
          </div>
        </div>
      </q-card>
    </section>
  </div>
</template>

<script setup></script>

<style scoped>
.my-card {
  padding: 25px;
}

.card-wrapper {
  margin-left: 7px;
}
.my-card .icon {
  width: 69px;
  height: 69px;
  background-color: #e4f6f0;
  padding: 10px;
  border-radius: 50%;
  object-fit: contain;
  margin: auto;
  margin-top: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  position: relative;
}

.my-card .text_class {
  color: #464255;
  display: block;
  line-height: 1.2;
}

.my-card #headline {
  font-size: 45px;
}

.my-card #description {
  font-size: 14px;
}

.my-card .percentage {
  color: #a3a3a3;
  font-size: 12px;
}
</style>
