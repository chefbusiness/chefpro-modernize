import CounterStat from './CounterStat';

export default function SocialProofStrip() {
  return (
    <section className="border-y bg-muted/30 py-12">
      <div className="container">
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-8 text-center">
          <CounterStat 
            end={55} 
            suffix="+" 
            label="Apps Especializadas"
          />
          <CounterStat 
            end={25} 
            suffix="+" 
            label="Cocinas del Mundo"
          />
          <CounterStat 
            end={6} 
            suffix="+" 
            label="Categorías Profesionales"
          />
          <CounterStat 
            end={1} 
            suffix="" 
            label="App Nueva cada Semana"
          />
          <div className="col-span-2 md:col-span-4 lg:col-span-1">
            <CounterStat 
              end={10000} 
              suffix="+" 
              label="Chefs Confían en Nosotros"
            />
          </div>
        </div>
      </div>
    </section>
  );
}