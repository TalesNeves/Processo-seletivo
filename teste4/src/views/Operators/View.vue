<template>
   <div>
    <div class="card">
       <input placeholder="Razão Social" v-model="data.lookforterm" type="text" class="form-control"/>
       <button @click="getByRazao" type="button" class="btn btn-primary">Procurar</button>
      <div class="card-header">
        <h4>
          Operadoras

        </h4>
      </div>
      <div class="table-responsive card-body">
        <table class="table table-hover table-bordered">
          <thead>
           <tr>
        <th>reg_ans</th>
        <th>cnpj</th>
        <th>razao_social</th>
        <th>nome_fantasia </th>
        <th>modalidade</th>
        <th>logradouro</th>
        <th>numero</th>
        <th>complemento</th>
        <th>bairro</th>
        <th>cidade</th>
        <th>uf</th>
        <th>cep</th>
        <th>ddd</th>
        <th>telefone</th>
        <th>fax</th>
        <th>email</th>
        <th>representante</th>
        <th>cargo_representant</th>
        <th>data_registro_ans</th>
        
            </tr>
          </thead>
          <tbody>
            <tr v-for="(operadora,index) in this.data.operadoras" :key="index">
        <td>{{operadora.reg_ans}}</td>
        <td>{{operadora.cnpj}}</td>
        <td>{{operadora.razao_social}}</td>
        <td>{{operadora.nome_fantasia }}</td>
        <td>{{operadora.modalidade}}</td>
        <td>{{operadora.logradouro}}</td>
        <td>{{operadora.numero}}</td>
        <td>{{operadora.complemento}}</td>
        <td>{{operadora.bairro}}</td>
        <td>{{operadora.cidade}}</td>
        <td>{{operadora.uf}}</td>
        <td>{{operadora.cep}}</td>
        <td>{{operadora.ddd}}</td>
        <td>{{operadora.telefone}}</td>
        <td>{{operadora.fax}}</td>
        <td>{{operadora.email}}</td>
        <td>{{operadora.representante}}</td>
        <td>{{operadora.cargo_representant}}</td>
        <td>{{operadora.data_registro_ans}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
   </div>
  
</template>

<script>
import axios from 'axios'

export default{

  name: 'operadoras',
  data(){
    return{
    
      data:{
        operadoras: [],
        lookforterm: ""
      }
        
    }
  },
  mounted(){
    this.getOperadoras();
  },
  methods:{
    getOperadoras(){
      axios.get('http://ec2-18-118-189-190.us-east-2.compute.amazonaws.com:5000/all').then(res => {
        this.data.operadoras = res.data
      });
    },
    getByRazao(){
      axios.get('http://ec2-18-118-189-190.us-east-2.compute.amazonaws.com:5000/like/'+this.data.lookforterm).then(res => {
        this.data.operadoras = res.data
      });
    }
  }
}
</script>

<style>
.table-responsive::-webkit-scrollbar {
    -webkit-appearance: none;
}

.table-responsive::-webkit-scrollbar:vertical {
    width: 12px;
}

.table-responsive::-webkit-scrollbar:horizontal {
    height: 12px;
}

.table-responsive::-webkit-scrollbar-thumb {
    background-color: rgba(0, 0, 0, .5);
    border-radius: 10px;
    border: 2px solid #ffffff;
}

.table-responsive::-webkit-scrollbar-track {
    border-radius: 10px;  
    background-color: #ffffff; 
}
table {
        width: 100%;
    }

/* tbody { display: flex; } */

/* tr:after {
    content: ' ';
    display: block;
    visibility: hidden;
    clear: both;
}

thead th {
    height: 30px;

    /*text-align: left;*/


/* tbody {
    height: 220px;
    overflow-y: auto;
} */




/* thead th {
    width: 19.5%;
    float: left;
}
tbody td {
    width: 20%;
    float: left;
} */ 

/* .table-responsive {
 /* height: 100vh; */
 /* width: 100vw; */
 /* overflow: auto; */

</style>