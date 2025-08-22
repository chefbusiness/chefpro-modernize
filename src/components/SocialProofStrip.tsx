import CounterStat from './CounterStat';

export default function SocialProofStrip() {
  return (
    <section className="border-y bg-muted/30 py-12">
      <div className="container">
        <div className="grid grid-cols-2 gap-4 sm:gap-6 md:grid-cols-4 lg:grid-cols-5 lg:gap-8 text-center">
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
          <div className="col-span-2 md:col-span-1">
            <CounterStat 
              end={6} 
              suffix="+" 
              label="Categorías Profesionales"
            />
          </div>
          <div className="col-span-2 md:col-span-1">
            <CounterStat 
              end={1} 
              suffix="" 
              label="App Nueva cada Semana"
            />
          </div>
          <div className="col-span-2 md:col-span-4 lg:col-span-1">
            <CounterStat 
              end={10000} 
              suffix="+" 
              label="Chefs Confían"
            />
          </div>
        </div>
      </div>
    </section>
  );
}