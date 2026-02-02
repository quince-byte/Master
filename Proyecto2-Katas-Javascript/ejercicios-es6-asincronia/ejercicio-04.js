// 4.1 Mayores que 18
const ages = [22, 14, 24, 55, 65, 21, 12, 13, 90];
const adults = ages.filter(age => age > 18);
console.log(adults);

// 4.2 Pares
const evens = ages.filter(age => age % 2 === 0);
console.log(evens);

// 4.3 Streamers de LoL
const streamers = [
	{name: 'Rubius', age: 32, gameMorePlayed: 'Minecraft'},
	{name: 'Ibai', age: 25, gameMorePlayed: 'League of Legends'},
	{name: 'Reven', age: 43, gameMorePlayed: 'League of Legends'},
	{name: 'AuronPlay', age: 33, gameMorePlayed: 'Among Us'}
];
const lolStreamers = streamers.filter(streamer => streamer.gameMorePlayed === 'League of Legends');
console.log(lolStreamers);

// 4.4 Nombre que incluye 'u'
const uStreamers = streamers.filter(streamer => streamer.name.includes('u'));
console.log(uStreamers);

// 4.5 Filter 'Legends' y mutación condicional
const legendsStreamers = streamers
    .filter(streamer => streamer.gameMorePlayed.includes('Legends'))
    .map(streamer => {
        if (streamer.age > 35) {
            return { ...streamer, gameMorePlayed: streamer.gameMorePlayed.toUpperCase() };
        }
        return streamer;
    });

console.log(legendsStreamers);