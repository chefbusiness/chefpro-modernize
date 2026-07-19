import type { Config } from "tailwindcss";

export default {
	darkMode: ["class"],
	content: [
		"./src/**/*.{astro,html,md,mdx,js,jsx,ts,tsx}",
		// Fase 5 (zona app islands): los componentes de la SPA importados
		// cross-root deben entrar en el scan de Tailwind o sus clases se
		// purgarían del CSS final. Globs acotados al cierre de imports de la
		// zona app (censo 2026-07-19, 107 ficheros); shared/** escanea también
		// algunos shared de marketing fuera del cierre — inflado de CSS
		// marginal, aceptado a cambio de un glob simple. NO abrir a ../src/**.
		"../src/pages/*AccessGate.tsx",
		"../src/pages/*Dashboard.tsx",
		"../src/pages/ProPromptsLibrary.tsx",
		"../src/pages/AdminGenerateAccess.tsx",
		"../src/components/shared/**/*.tsx",
		"../src/components/library/**/*.tsx",
		// Fase 6 (marketing/legales islands): cierre de imports = 22 páginas +
		// components top-level (ModernHeader/Footer, PricingPlans, OtherFreeTools,
		// HeroSocialProof, AnnouncementBar…) + ui. Censo 2026-07-19, 56 ficheros
		// (scripts/astro-migration/fase6-*). Sigue sin abrirse ../src/** entero.
		"../src/pages/{CalculadoraBrigada,CalculadoraFoodCost,CalendarioContenidos,ChatGPTRestaurantes,DetectorAlergenos,EscandallosRestaurante,GeneradorMenuDegustacion,GeneradorTextosCarta,HerramientasGratuitas,HerramientasIARestaurantes,MarketingRestaurante,MenuRestaurante,RecetasIARestaurantes,ReducirCostesRestaurante,SimuladorRentabilidad,SoftwareGestionCocina,TestDigitalizacion,Legal,Cookies,Privacy,Terms,SistemaCreditos}.tsx",
		"../src/components/*.tsx",
		"../src/components/ui/*.tsx",
	],
	prefix: "",
	theme: {
		container: {
			center: true,
			padding: '2rem',
			screens: {
				'2xl': '1400px'
			}
		},
		extend: {
			fontFamily: {
				sans: ['Inter', 'system-ui', 'sans-serif'],
			},
			colors: {
				border: 'hsl(var(--border))',
				input: 'hsl(var(--input))',
				ring: 'hsl(var(--ring))',
				background: 'hsl(var(--background))',
				foreground: 'hsl(var(--foreground))',
				primary: {
					DEFAULT: 'hsl(var(--primary))',
					foreground: 'hsl(var(--primary-foreground))',
					hover: 'hsl(var(--primary-hover))'
				},
				secondary: {
					DEFAULT: 'hsl(var(--secondary))',
					foreground: 'hsl(var(--secondary-foreground))'
				},
				destructive: {
					DEFAULT: 'hsl(var(--destructive))',
					foreground: 'hsl(var(--destructive-foreground))'
				},
				muted: {
					DEFAULT: 'hsl(var(--muted))',
					foreground: 'hsl(var(--muted-foreground))'
				},
				accent: {
					DEFAULT: 'hsl(var(--accent))',
					foreground: 'hsl(var(--accent-foreground))',
					light: 'hsl(var(--accent-light))',
					dark: 'hsl(var(--accent-dark))'
				},
				popover: {
					DEFAULT: 'hsl(var(--popover))',
					foreground: 'hsl(var(--popover-foreground))'
				},
				card: {
					DEFAULT: 'hsl(var(--card))',
					foreground: 'hsl(var(--card-foreground))'
				},
				chef: {
					gold: 'hsl(var(--chef-gold))',
					dark: 'hsl(var(--chef-dark))',
					blue: 'hsl(var(--chef-blue))',
					gray: 'hsl(var(--chef-gray))'
				},
				sidebar: {
					DEFAULT: 'hsl(var(--sidebar-background))',
					foreground: 'hsl(var(--sidebar-foreground))',
					primary: 'hsl(var(--sidebar-primary))',
					'primary-foreground': 'hsl(var(--sidebar-primary-foreground))',
					accent: 'hsl(var(--sidebar-accent))',
					'accent-foreground': 'hsl(var(--sidebar-accent-foreground))',
					border: 'hsl(var(--sidebar-border))',
					ring: 'hsl(var(--sidebar-ring))'
				}
			},
			backgroundImage: {
				'gradient-hero': 'var(--gradient-hero)',
				'gradient-card': 'var(--gradient-card)',
				'gradient-cta': 'var(--gradient-cta)'
			},
			boxShadow: {
				'elegant': 'var(--shadow-elegant)',
				'glow': 'var(--shadow-glow)',
				'card': 'var(--shadow-card)'
			},
			borderRadius: {
				lg: 'var(--radius)',
				md: 'calc(var(--radius) - 2px)',
				sm: 'calc(var(--radius) - 4px)'
			},
			keyframes: {
				'accordion-down': {
					from: {
						height: '0'
					},
					to: {
						height: 'var(--radix-accordion-content-height)'
					}
				},
				'accordion-up': {
					from: {
						height: 'var(--radix-accordion-content-height)'
					},
					to: {
						height: '0'
					}
				},
				marquee: {
					'0%': { transform: 'translateX(0)' },
					'100%': { transform: 'translateX(-50%)' },
				},
				'marquee-reverse': {
					'0%': { transform: 'translateX(-50%)' },
					'100%': { transform: 'translateX(0)' },
				},
			},
			animation: {
				'accordion-down': 'accordion-down 0.2s ease-out',
				'accordion-up': 'accordion-up 0.2s ease-out',
				marquee: 'marquee linear infinite',
				'marquee-reverse': 'marquee-reverse linear infinite',
			}
		}
	},
	plugins: [require("tailwindcss-animate")],
} satisfies Config;
