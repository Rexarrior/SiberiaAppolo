<template>

  <div class=e0_3>
    <b-container class="task1-form">
      <b-card>
        <h5 class="card-title">Валидация сертификата</h5>
        <b-form @submit="onSubmit" @reset="onReset">

          <b-form-group id="input-group-1" label="Коды ТН ВЭД ЕАЭС" label-for="input-1">
            <b-form-input id="input-1" v-model="form1.tnved" placeholder="" required></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Технические регламенты" label-for="input-2">
            <b-form-input id="input-2" v-model="form1.reglament" placeholder="" required></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Группа продукции" label-for="input-3">
            <b-form-input id="input-3" v-model="form1.group" placeholder="" required></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-4" label="Наименование продукции" label-for="input-4">
            <b-form-input id="input-4" v-model="form1.productName" placeholder="" required></b-form-input>
          </b-form-group>


          <b-button class="form-button" type="submit" variant="primary">Валидировать!</b-button>
          <b-button class="form-button" type="reset" variant="primary">Загрузить файл</b-button>
        </b-form>
        <b-card class="mt-3" header="Результат" v-if="show">
          <pre class="m-0">{{ task1_answer }}</pre>
        </b-card>
      </b-card>
    </b-container>

    <b-container class="task2-form">
      <b-card>
        <h5 class="card-title">Рекомендации по названию продукции</h5>
        <b-form @submit="onSubmit" @reset="onReset">


          <b-form-group id="input-group-1" label="Наименование продукции" label-for="input-1">
            <b-form-input id="input-1" v-model="form2.productName" placeholder="" required></b-form-input>
          </b-form-group>


          <b-button class="form-button" type="submit" variant="primary">Получить Рекомендации!</b-button>
        </b-form>
        <b-card class="mt-3" header="Результат" v-if="show">
          <pre class="m-0">{{ task2_answer }}</pre>
        </b-card>
      </b-card>
    </b-container>

    <!-- <b-container class="task3-form">
      <b-card>
        <h5 class="card-title">Интерактивная карта товаров</h5>
        <b-form @submit="onSubmit" @reset="onReset">


          <b-form-group id="input-group-1" label="Наименование продукции" label-for="input-1">
            <b-form-input id="input-1" v-model="form3.productName" placeholder="" required></b-form-input>
          </b-form-group>


          <b-button class="form-button" type="submit" variant="primary">Получить Рекомендации!</b-button>
        </b-form>
        <b-card class="mt-3" header="Form Data Result" v-if="show">
          <MapExample></MapExample>
        </b-card>
      </b-card>
    </b-container> -->
    <div class=e33_53>
      <div class="e4_7"></div><span class="e4_8">ИНФРАСТРУКТУРА ДОВЕРИЯ</span><span class="e4_9">О
        РОСАККРЕДИТАЦИИ</span><span class="e4_10">НИАР</span><span class="e4_11">ТЕХНОЛОГИЧНОСТЬ</span><span
        class="e4_12">КОМПЕТЕНТНОСТЬ</span><span class="e4_13">ПРЕСС-ЦЕНТР</span><span
        class="e4_14">ДОКУМЕНТЫ</span><span class="e4_15">ОБРАТНАЯ СВЯЗЬ</span>
    </div>
    <div class=e33_48>
      <div class="e4_2"></div>
    </div>
    <div class=e33_46>
      <div class="e4_4"></div>
    </div>
    <div class=e33_47>
      <div class="e4_3"></div>
    </div>
    <div class=e33_45>
      <div class="e4_5"></div>
    </div>
  </div>
</template>

<script>
// import MapExample from './MapExample.vue'
// import axios from "axios"
// import { response } from "express"
// import  consts from "../js/common.js"
// import tools from "../js/tools.js"


export default {
  name: "indexOne",
  data() {
    return {
      form1: {
        tnved: "4016999708",
        reglament: "ТР ЕАЭС 043/2017 О требованиях к средствам обеспечения пожарной безопасности и пожаротушения",
        group: "Узлы пересечения противопожарных преград кабельными изделиями, шинопроводами, герметичными кабельными вводами, муфтами и трубопроводами инженерных систем зданий и сооружений",
        productName: "Проходки кабельные модульные универсальные огнестойкие типа КП-90, габаритными размерами 580х540 мм, общей толщиной 320 мм, состоящие из стальной рамки из угловых профилей (ГОСТ 8509-86), 8 закрепительных анкерных пластин (ГОСТ 8509-86), уплотнительных огнестойких модулей с цельнорезиновым сердечником типа РМ (глубиной 60 мм с каждой стороны) и компрессионных блоков типа РВ (глубиной 60 мм с каждой стороны). Пространство 200 мм между двумя проходками заполнено минеральной ватой "
      },
      form2: {
        productName: "Насосы шестеренные EnviroGear"
      },
      task2_answer: {
        tnved: "6302210000",
        reglament: "ТР ЕАЭС 043/2017 О требованиях к средствам обеспечения пожарной безопасности и пожаротушения",
        group: "Электрическое (электрооборудование) и неэлектрическое оборудование для работы во взрывоопасных средах, применяемое на опасных производственных объектах, за исключением изделий медицинского назначения, оборудования, при эксплуатации которого опасность взрыва возникает только из-за наличия взрывоопасных веществ и нестойких химических соединений, оборудования, предназначенного для бытового и непроизводственного применения в условиях, когда взрывоопасная среда образуется вследствие непредвиденной утечки горючего газа, средств индивидуальной защиты, морских судов и морских платформ, кроме электрооборудования, находящегося на их борту во взрывоопасных зонах, транспортных средств общего пользования, предназначенных для перевозки пассажиров и грузов воздушным, наземным, железнодорожным или водным транспортом, ядерного оружия, исследовательских установок организаций ядерно- оборонного комплекса и связанных с ними процессами проектирования (разработки), производства, монтажа, наладки, эксплуатации, хранения, перевозки и утилизации",
        productName: "Насосы шестеренные EnviroGear"
      },
      show: true,
      task1_answer: {
        validation_score: 87.5
      }
    };
  },
  methods: {
    onSubmit() {
      //   event.preventDefault()
      //   let id = tools.uuidv4()
      //    axios({
      //         url: `${consts.SERVER_IP}/api/task1_form`,
      //         data: {"guid": id, "data": this.form1},
      //         method: 'POST',
      //         headers: {
      //             'Content-Type': 'application/json'
      //         }})
      // .then(response => ()=>{
      //   console.log(response)
      //   }).catch(reason => ()=>{
      //     console.log(reason);
      //   });
      //   axios({
      //       url: `${consts.SERVER_IP}/api/task1_form_result`,
      //       params: {id, "data": this.form1},
      //       method: 'POST',
      //     }
      //   ).then(response => ()=> {
      //     this.task1_answer = response.data
      //   this.show = true;
      //   })
    },
    onReset(event) {
      event.preventDefault();
    }
  },
  // components: { MapExample }
}
</script>

<style scoped>
.form-button {
  margin-right: 10px;
}

.task1-form {
  margin-top: 300px;
  width: 50%;
}

.task2-form {
  margin-top: 30px;
  width: 50%;
}

body {
  background: #E5E5E5;
}

.e0_3 {
  overflow: hidden;
}

.e0_3 {
  background-color: rgba(189.94232296943665, 188.76640766859055, 247.56250709295273, 1);
  width: 100%;
  height: 2000px;
  position: absolute;
}

.e33_58 {
  width: 939px;
  height: 76px;
  position: absolute;
  left: 1138px;
  top: 440px;
}

.e0_4 {
  color: rgba(49.310622811317444, 24.171878546476364, 69.0625025331974, 1);
  width: 939px;
  height: 76px;
  position: absolute;
  left: 0px;
  top: 0px;
  font-family: Inter;
  text-align: left;
  font-size: 64px;
  letter-spacing: 0;
}

.e33_57 {
  width: 938px;
  height: 306px;
  position: absolute;
  left: 120px;
  top: 502px;
}

.e0_5 {
  color: rgba(49.310622811317444, 24.171878546476364, 69.0625025331974, 1);
  width: 938px;
  height: 306px;
  position: absolute;
  left: 0px;
  top: 0px;
  font-family: Inter;
  text-align: left;
  font-size: 64px;
  letter-spacing: 0;
}

.e33_55 {
  width: 1519px;
  height: 89px;
  position: absolute;
  left: 120px;
  top: 984px;
}

.e0_7 {
  background-color: rgba(244.3749949336052, 215.86459279060364, 203.64583164453506, 1);
  width: 1196px;
  height: 89px;
  position: absolute;
  left: 0px;
  top: 0px;
  border-top-left-radius: 100px;
  border-top-right-radius: 100px;
  border-bottom-left-radius: 100px;
  border-bottom-right-radius: 100px;
}

.e0_8 {
  color: rgba(0, 0, 0, 1);
  width: 799px;
  height: 58px;
  position: absolute;
  left: 48px;
  top: 13px;
  font-family: Inter;
  text-align: left;
  font-size: 48px;
  letter-spacing: 0;
}

.e0_9 {
  width: 62px;
  height: 75px;
  position: absolute;
  left: 1095px;
  top: 7px;
  background-image: url(../assets/search__v1_1.png);
  background-repeat: no-repeat;
  background-size: cover;
}

.e0_10 {
  background-color: rgba(244.3749949336052, 215.86459279060364, 203.64583164453506, 1);
  width: 269px;
  height: 89px;
  position: absolute;
  left: 1250px;
  top: 0px;
  border-top-left-radius: 100px;
  border-top-right-radius: 100px;
  border-bottom-left-radius: 100px;
  border-bottom-right-radius: 100px;
}

.e0_11 {
  color: rgba(11.059297062456608, 11.68750025331974, 10.95703125, 1);
  width: 143px;
  height: 58px;
  position: absolute;
  left: 1313px;
  top: 16px;
  font-family: Inter;
  text-align: left;
  font-size: 48px;
  letter-spacing: 0;
}

.e33_56 {
  width: 500px;
  height: 58px;
  position: absolute;
  left: 168px;
  top: 1089px;
}

.e0_12 {
  color: rgba(49.310622811317444, 24.171878546476364, 69.0625025331974, 1);
  width: 500px;
  height: 58px;
  position: absolute;
  left: 0px;
  top: 0px;
  font-family: Inter;
  text-align: left;
  font-size: 48px;
  letter-spacing: 0;
}

.e33_53 {
  width: 1920px;
  height: 298px;
  position: absolute;
  left: 0px;
  top: 0px;
}

.e4_7 {
  background-color: rgba(178.98874193429947, 177.43749797344208, 255, 1);
  width: 1920px;
  height: 298px;
  position: absolute;
  left: 0px;
  top: 0px;
}

.e4_8 {
  color: rgba(49.00000087916851, 24.000000469386578, 69.00000348687172, 1);
  width: 279.8746032714844px;
  height: 24px;
  position: absolute;
  left: 120.37617492675781px;
  top: 265px;
  font-family: Irish Grover;
  text-align: left;
  font-size: 20px;
  letter-spacing: 0;
}

.e4_9 {
  color: rgba(49.00000087916851, 24.000000469386578, 69.00000348687172, 1);
  width: 221.6927947998047px;
  height: 24px;
  position: absolute;
  left: 444.3887023925781px;
  top: 265px;
  font-family: Irish Grover;
  text-align: left;
  font-size: 20px;
  letter-spacing: 0;
}

.e4_10 {
  color: rgba(49.00000087916851, 24.000000469386578, 69.00000348687172, 1);
  width: 56.1755485534668px;
  height: 24px;
  position: absolute;
  left: 708.2131958007812px;
  top: 267px;
  font-family: Irish Grover;
  text-align: left;
  font-size: 20px;
  letter-spacing: 0;
}

.e4_11 {
  color: rgba(49.00000087916851, 24.000000469386578, 69.00000348687172, 1);
  width: 201.63009643554688px;
  height: 24px;
  position: absolute;
  left: 800.5015869140625px;
  top: 268px;
  font-family: Irish Grover;
  text-align: left;
  font-size: 20px;
  letter-spacing: 0;
}

.e4_12 {
  color: rgba(49.00000087916851, 24.000000469386578, 69.00000348687172, 1);
  width: 187.58621215820312px;
  height: 24px;
  position: absolute;
  left: 1045.2664794921875px;
  top: 268px;
  font-family: Irish Grover;
  text-align: left;
  font-size: 20px;
  letter-spacing: 0;
}

.e4_13 {
  color: rgba(49.00000087916851, 24.000000469386578, 69.00000348687172, 1);
  width: 140px;
  height: 24px;
  position: absolute;
  left: 1276.9906005859375px;
  top: 271px;
  font-family: Irish Grover;
  text-align: left;
  font-size: 20px;
  letter-spacing: 0;
}

.e4_14 {
  color: rgba(49.00000087916851, 24.000000469386578, 69.00000348687172, 1);
  width: 127.39811706542969px;
  height: 24px;
  position: absolute;
  left: 1457.5548095703125px;
  top: 268px;
  font-family: Irish Grover;
  text-align: left;
  font-size: 20px;
  letter-spacing: 0;
}

.e4_15 {
  color: rgba(49.00000087916851, 24.000000469386578, 69.00000348687172, 1);
  width: 172.5391845703125px;
  height: 24px;
  position: absolute;
  left: 1625.078369140625px;
  top: 265px;
  font-family: Irish Grover;
  text-align: left;
  font-size: 20px;
  letter-spacing: 0;
}

.e33_48 {
  width: 293px;
  height: 99px;
  position: absolute;
  left: 133px;
  top: 58px;
}

.e4_2 {
  width: 293px;
  height: 99px;
  position: absolute;
  left: 0px;
  top: 0px;
  background-image: url(../assets/logo_1.png);
  background-repeat: no-repeat;
  background-size: cover;
}

.e33_46 {
  width: 159px;
  height: 99px;
  position: absolute;
  left: 1323px;
  top: 58px;
}

.e4_4 {
  width: 159px;
  height: 99px;
  position: absolute;
  left: 0px;
  top: 0px;
  background-image: url(../assets/2_1.png);
  background-repeat: no-repeat;
  background-size: cover;
}

.e33_47 {
  width: 100px;
  height: 99px;
  position: absolute;
  left: 1165px;
  top: 58px;
}

.e4_3 {
  width: 100px;
  height: 99px;
  position: absolute;
  left: 0px;
  top: 0px;
  background-image: url(../assets/ilac_new_1.png);
  background-repeat: no-repeat;
  background-size: cover;
}

.e33_45 {
  width: 254px;
  height: 99px;
  position: absolute;
  left: 1540px;
  top: 58px;
}

.e4_5 {
  width: 254px;
  height: 99px;
  position: absolute;
  left: 0px;
  top: 0px;
  background-image: url(../assets/3_1.png);
  background-repeat: no-repeat;
  background-size: cover;
}
</style>