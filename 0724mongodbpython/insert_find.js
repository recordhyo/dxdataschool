show dbs

use parkhs

db.users.insert({name:"park",age:25,gender:"woman"})

db.users.insert([{name:"kim",age:22,gender:"man"},{name:"lee",age:27,gender:"man"}])

db.users.find()

show dbs

db.sample.createIndex({name:1},{unique:true})


db.sample.insert({name:"park"})


db.sample.insert([{name:"kim"},{name:"park"},{name:"lee"}])

db.sample.find()

-- 멀티스레드로삽입
db.sample.insert([{name:"lee"},{name:"park"},{name:"choi"}],{ordered:false})

db.sample.find()


db.sample.insertOne({name:"yun"})
db.sample.find()


db.sample.insertOne({name:"lim",score:76})
db.sample.find()


var num =1 
for(var i =0; i<3; i++){
	db.sample.insertOne({name:"user"+i, score:num})
};

db.sample.find()

db.area.find()

db.by_type.find()


db.users.find({name:"park", age:25})


//샘플 데이터 삽입
db.containerBox.insertMany([ 
{name:"bear", weight:60, category:"animal"},
{name:"bear", weight:10, category:"animal"},
{name:"cat", weight:15, category:"animal"},
{name:"phone", weight:1, category:"electronic"}])

db.containerBox.find({category:"animal"})

use parkhs;

db.containerBox.find({category:'animal', name:'bear'})

db.containerBox.find({},{_id:true, name:1})
db.containerBox.find({},{name:0})

db.inventory.find()

db.inventory.find({tags:{$in:['black','blue']}})

db.inventory.find({tags:{$in:[/^[a-z]|a/]}})

db.inventory.find({qty:{$not:{$gt:2}}})

db.inventory.find({$or:[{qty:{$gt:100}}, {qty:{$lt:10}}]})





db.users.insert({name:'paulo'})
db.users.insert({name:'patric'})
db.users.insert({name:'pedro'})

//r을 포함하는
db.users.find({name:/r/})

//pa로 시작하는
db.users.find({name:/^pa/})

//ro로 끝나는
db.users.find({name:/ro$/})



//샘플 데이터 삽입
db.inventory.insertMany([
{ item: "journal", qty: 25, tags: ["blank", "red"] },
{ item: "notebook", qty: 50, tags: ["red", "blank"] },
{ item: "paper", qty: 100, tags:[]},
{ item: "planner", qty: 75, tags: ["blank", "red"] },
{ item: "postcard", qty: 45, tags: ["blue"] }
]);

//배열로 조회하면 순서도 맞아야함
db.inventory.find({tags:["red", "blank"]})


//인덱스 조회 (슬라이스)
db.inventory.find({},{tags:{$slice:[0,2]}})


//샘플 데이터 삽입
db.users.insert({name:"matt", scores:[79, 85, 93]})
db.users.insert({name:"lara", scores:[91, 74, 63]})

//모든값이 80보다 크고 90보다 작아야 조회됨
db.users.find({scores:{$gt:80, $lt:90}})


//하나라도 80보다 크고 90보다 작은 데이터 조회
db.users.find({scores:{$elemMatch:{$gt:80, $lt:90}}})


//순서 상관없이 데이터만 포함하고 있으면 조회
db.inventory.find({tags:{$all:["red","blank"]}})


//데이터 없는 것 조회 (size=0이면 조회)
db.inventory.find({tags:{$size:0}})


//skip과 limit 함께 사용 가능
db.inventory.find().skip(2).limit(2)


//id에 대한 오름차순 정렬
db.inventory.find().sort({id:1})



var cursor = db.inventory.find();

//다음 데이터 존재 여부
cursor.hasNext();

//다음 데이터 가져오기
cursor.next();

//삼항연산자
cursor.hasNext() ? cursor.next() : null
