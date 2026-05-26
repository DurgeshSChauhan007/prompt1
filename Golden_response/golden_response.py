'''

import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

// ==========================================
// 1. MOCK DATABASE & BACKEND ARCHITECTURE (In-Memory)
// ==========================================

const MOCK_VEHICLES = [
  { id: 'v1', brand: 'Tesla', model: 'Model S Plaid', category: 'Luxury', transmission: 'Automatic', fuelType: 'Electric', seats: 5, pricePerDay: 149, rating: 4.9, image: 'https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?auto=format&fit=crop&w=600&q=80', status: 'Available', location: 'Los Angeles' },
  { id: 'v2', brand: 'Porsche', model: '911 Carrera S', category: 'Sport', transmission: 'Automatic', fuelType: 'Petrol', seats: 4, pricePerDay: 299, rating: 5.0, image: 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=600&q=80', status: 'Available', location: 'Miami' },
  { id: 'v3', brand: 'Range Rover', model: 'Sport', category: 'SUV', transmission: 'Automatic', fuelType: 'Hybrid', seats: 7, pricePerDay: 189, rating: 4.8, image: 'https://images.unsplash.com/photo-1606016159991-dfe4f2746ad5?auto=format&fit=crop&w=600&q=80', status: 'Available', location: 'New York' },
  { id: 'v4', brand: 'Audi', model: 'e-tron GT', category: 'Luxury', transmission: 'Automatic', fuelType: 'Electric', seats: 5, pricePerDay: 169, rating: 4.7, image: 'https://images.unsplash.com/photo-1617788138017-80ad40651399?auto=format&fit=crop&w=600&q=80', status: 'Maintenance', location: 'Los Angeles' },
];

const mockDatabase = {
  vehicles: [...MOCK_VEHICLES],
  bookings: [
    { id: 'b1', userId: 'u1', vehicleId: 'v1', totalAmount: 447, bookingStatus: 'Confirmed', paymentStatus: 'Paid', pickupDate: '2026-06-01', returnDate: '2026-06-04' }
  ],
  inquiries: [],
  users: [{ id: 'u1', name: 'John Doe', email: 'john@example.com', role: 'Customer' }]
};

// Simulated JWT API Network Request Layer
const apiFetch = async (endpoint, options = {}) => {
  await new Promise(resolve => setTimeout(resolve, 400)); // Simulate 400ms network latency
  const body = options.body ? JSON.parse(options.body) : null;

  switch(endpoint) {
    case '/api/bookings/create':
      const newBooking = {
        id: `b_${Math.random().toString(36).substr(2, 9)}`,
        ...body,
        bookingStatus: 'Confirmed',
        paymentStatus: 'Paid'
      };
      mockDatabase.bookings.push(newBooking);
      return { success: true, data: newBooking };
    case '/api/inquiries':
      const newInquiry = { id: `i_${Math.random().toString(36).substr(2, 9)}`, ...body, createdAt: new Date() };
      mockDatabase.inquiries.push(newInquiry);
      return { success: true, message: "Inquiry submitted securely." };
    case '/api/admin/analytics':
      const totalRevenue = mockDatabase.bookings.reduce((acc, curr) => acc + curr.totalAmount, 0);
      return { success: true, data: { revenue: totalRevenue, totalBookings: mockDatabase.bookings.length, activeFleet: mockDatabase.vehicles.length } };
    default:
      return { error: "404 Not Found" };
  }
};

// ==========================================
// 2. ANIMATION VARIANT CONFIGURATIONS (60FPS optimization)
// ==========================================
const faderUp = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: [0.25, 1, 0.5, 1] } }
};

const staggerContainer = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { staggerChildren: 0.1 } }
};

const modalVariants = {
  hidden: { opacity: 0, scale: 0.95 },
  visible: { opacity: 1, scale: 1, transition: { duration: 0.3, ease: "easeOut" } },
  exit: { opacity: 0, scale: 0.95, transition: { duration: 0.2, ease: "easeIn" } }
};

// ==========================================
// 3. MAIN INTERFACE COMPONENT
// ==========================================
export default function FullStackCarPlatform() {
  const [currentTab, setCurrentTab] = useState('browse'); // browse | admin | dashboard
  const [vehicles, setVehicles] = useState(mockDatabase.vehicles);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [selectedVehicle, setSelectedVehicle] = useState(null);
  
  // Booking Workflow State
  const [bookingStep, setBookingStep] = useState(1);
  const [formData, setFormData] = useState({ pickup: 'Los Angeles', dropoff: 'Los Angeles', days: 3, insurance: true });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);
  
  // Admin & Analytics State
  const [analytics, setAnalytics] = useState({ revenue: 447, totalBookings: 1, activeFleet: 4 });

  useEffect(() => {
    const loadAnalytics = async () => {
      const res = await apiFetch('/api/admin/analytics');
      if (res.success) setAnalytics(res.data);
    };
    loadAnalytics();
  }, [vehicles, isSuccess]);

  // Handle Search Filtering
  const filteredVehicles = vehicles.filter(v => {
    const matchesSearch = v.brand.toLowerCase().includes(searchQuery.toLowerCase()) || v.model.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesCat = selectedCategory === 'All' || v.category === selectedCategory;
    return matchesSearch && matchesCat;
  });

  const handleExecuteBooking = async () => {
    setIsSubmitting(true);
    const amount = (selectedVehicle.pricePerDay * formData.days) + (formData.insurance ? 25 * formData.days : 0);
    
    const payload = {
      userId: 'u1',
      vehicleId: selectedVehicle.id,
      pickupLocation: formData.pickup,
      dropoffLocation: formData.dropoff,
      totalAmount: amount,
    };

    const response = await apiFetch('/api/bookings/create', {
      method: 'POST',
      body: JSON.stringify(payload)
    });

    if (response.success) {
      setIsSubmitting(false);
      setIsSuccess(true);
      setTimeout(() => {
        setIsSuccess(false);
        setSelectedVehicle(null);
        setBookingStep(1);
        setCurrentTab('dashboard');
      }, 2000);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 font-sans antialiased selection:bg-amber-500 selection:text-black">
      
      {/* GLOBAL NAVBAR */}
      <nav className="sticky top-0 z-40 bg-slate-900/80 backdrop-blur-md border-b border-slate-800 px-6 py-4 flex justify-between items-center">
        <div className="flex items-center space-x-2">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-amber-500 to-orange-600 flex items-center justify-center font-bold text-black text-sm tracking-wider">V</div>
          <span className="text-xl font-bold tracking-tight bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">VELOCITY</span>
        </div>
        <div className="flex bg-slate-950 p-1 rounded-full border border-slate-800">
          <button onClick={() => setCurrentTab('browse')} className={`px-4 py-1.5 rounded-full text-xs font-medium transition-all ${currentTab === 'browse' ? 'bg-amber-500 text-black font-semibold' : 'text-slate-400 hover:text-white'}`}>Explore Fleet</button>
          <button onClick={() => setCurrentTab('dashboard')} className={`px-4 py-1.5 rounded-full text-xs font-medium transition-all ${currentTab === 'dashboard' ? 'bg-amber-500 text-black font-semibold' : 'text-slate-400 hover:text-white'}`}>My Dashboard</button>
          <button onClick={() => setCurrentTab('admin')} className={`px-4 py-1.5 rounded-full text-xs font-medium transition-all ${currentTab === 'admin' ? 'bg-amber-500 text-black font-semibold' : 'text-slate-400 hover:text-white'}`}>Admin Panel</button>
        </div>
      </nav>

      {/* RENDER DYNAMIC PAGES VIA ROUTER SYSTEM */}
      <main className="max-w-7xl mx-auto px-4 py-8">
        <AnimatePresence mode="wait">
          
          {/* VEHICLE BROWSE & DISCOVERY PAGE */}
          {currentTab === 'browse' && (
            <motion.div key="browse" initial="hidden" animate="visible" exit={{ opacity: 0 }} variants={staggerContainer}>
              
              {/* HERO SECTION */}
              <motion.section variants={faderUp} className="text-center py-12 px-4 rounded-3xl bg-gradient-to-b from-slate-900 via-slate-950 to-transparent border border-slate-900 mb-12">
                <span className="text-xs tracking-widest font-semibold text-amber-500 uppercase bg-amber-500/10 px-3 py-1 rounded-full">Premium Fleet Systems</span>
                <h1 className="text-4xl md:text-6xl font-black mt-4 tracking-tight leading-none">Drive the Unrivaled Experience.</h1>
                <p className="text-slate-400 max-w-xl mx-auto mt-4 text-sm md:text-base">High-performance motion-driven vehicle selection, real-time programmatic fleet scheduling, and instant secure bookings.</p>
              </motion.section>

              {/* FILTERING AND SEARCH UTILITIES */}
              <motion.div variants={faderUp} className="flex flex-col md:flex-row gap-4 items-center justify-between mb-8 bg-slate-900/50 p-4 rounded-2xl border border-slate-800/60">
                <input 
                  type="text" 
                  placeholder="Search brand, model, electric..." 
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full md:w-80 bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:border-amber-500 transition-colors"
                />
                <div className="flex gap-2 overflow-x-auto w-full md:w-auto pb-2 md:pb-0">
                  {['All', 'Luxury', 'Sport', 'SUV'].map(cat => (
                    <button 
                      key={cat} 
                      onClick={() => setSelectedCategory(cat)}
                      className={`px-4 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all ${selectedCategory === cat ? 'bg-slate-100 text-black' : 'bg-slate-950 border border-slate-800 text-slate-400'}`}
                    >
                      {cat}
                    </button>
                  ))}
                </div>
              </motion.div>

              {/* FLEET GRID ANIMATION */}
              <motion.div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {filteredVehicles.map(vehicle => (
                  <motion.div 
                    key={vehicle.id} 
                    variants={faderUp} 
                    whileHover={{ y: -6 }}
                    className="bg-slate-900 border border-slate-800/80 rounded-2xl overflow-hidden group flex flex-col justify-between"
                  >
                    <div className="relative overflow-hidden h-48 bg-slate-950">
                      <img src={vehicle.image} alt={vehicle.model} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-90 group-hover:opacity-100" />
                      <div className="absolute top-3 left-3 bg-black/60 backdrop-blur-md text-[10px] uppercase tracking-wider px-2.5 py-1 rounded-md border border-white/10 font-bold">
                        {vehicle.category}
                      </div>
                    </div>
                    <div className="p-5 flex-1 flex flex-col justify-between">
                      <div>
                        <div className="flex justify-between items-start mb-2">
                          <h3 className="text-lg font-bold tracking-tight text-white">{vehicle.brand} <span className="text-slate-400 font-normal">{vehicle.model}</span></h3>
                          <span className="text-xs text-amber-500 bg-amber-500/10 px-2 py-0.5 rounded font-mono">★ {vehicle.rating}</span>
                        </div>
                        <div className="grid grid-cols-2 gap-y-2 gap-x-4 py-3 my-2 border-y border-slate-800 text-xs text-slate-400">
                          <div>⚡ {vehicle.fuelType}</div>
                          <div>⚙️ {vehicle.transmission}</div>
                          <div>👥 {vehicle.seats} Seats</div>
                          <div>📍 {vehicle.location}</div>
                        </div>
                      </div>
                      <div className="flex justify-between items-center pt-3 mt-2">
                        <div>
                          <span className="text-xl font-black text-white">${vehicle.pricePerDay}</span>
                          <span className="text-xs text-slate-500"> / day</span>
                        </div>
                        <button 
                          onClick={() => setSelectedVehicle(vehicle)}
                          disabled={vehicle.status === 'Maintenance'}
                          className={`px-4 py-2 rounded-xl text-xs font-bold tracking-tight transition-all ${vehicle.status === 'Maintenance' ? 'bg-slate-800 text-slate-500 cursor-not-allowed' : 'bg-amber-500 hover:bg-amber-400 text-black'}`}
                        >
                          {vehicle.status === 'Maintenance' ? 'Maintenance' : 'Reserve Vehicle'}
                        </button>
                      </div>
                    </div>
                  </motion.div>
                ))}
              </motion.div>
            </motion.div>
          )}

          {/* USER RESERVATION DASHBOARD VIEW */}
          {currentTab === 'dashboard' && (
            <motion.div key="dashboard" initial="hidden" animate="visible" exit={{ opacity: 0 }} variants={faderUp} className="space-y-6">
              <div className="border-b border-slate-800 pb-4">
                <h2 className="text-2xl font-black tracking-tight">User Enterprise Dashboard</h2>
                <p className="text-slate-400 text-xs">Verify continuous rental schedules, transaction status, and telemetry updates.</p>
              </div>
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">
                <h3 className="text-sm font-bold uppercase tracking-wider text-slate-400 mb-4">Active & Confirmed Rentals</h3>
                <div className="space-y-4">
                  {mockDatabase.bookings.map(booking => {
                    const car = mockDatabase.vehicles.find(v => v.id === booking.vehicleId);
                    return (
                      <div key={booking.id} className="bg-slate-950 p-4 border border-slate-800 rounded-xl flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                        <div className="flex items-center gap-4">
                          <img src={car?.image} className="w-16 h-12 rounded-lg object-cover bg-slate-900" alt="" />
                          <div>
                            <h4 className="font-bold text-sm">{car?.brand} {car?.model}</h4>
                            <p className="text-xs text-slate-500">Timeline: {booking.pickupDate} to {booking.returnDate}</p>
                          </div>
                        </div>
                        <div className="flex gap-4 items-center w-full md:w-auto justify-between md:justify-end">
                          <div className="text-right">
                            <span className="text-xs block text-slate-400 font-mono">Invoice Value</span>
                            <span className="text-sm font-extrabold text-white">${booking.totalAmount}</span>
                          </div>
                          <span className="px-3 py-1 rounded-full text-[10px] uppercase tracking-wider font-extrabold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                            {booking.bookingStatus} & {booking.paymentStatus}
                          </span>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            </motion.div>
          )}

          {/* REVENUE & FLEET ADMINISTRATIVE DASHBOARD */}
          {currentTab === 'admin' && (
            <motion.div key="admin" initial="hidden" animate="visible" exit={{ opacity: 0 }} variants={faderUp} className="space-y-8">
              <div>
                <h2 className="text-2xl font-black tracking-tight">System Infrastructure Analytics</h2>
                <p className="text-slate-400 text-xs">Mission-critical pipeline state, performance matrices, and billing logs.</p>
              </div>

              {/* ANALYTICS HIGHLIGHT METRICS */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-500 block">Gross Processed Revenue</span>
                  <span className="text-3xl font-black text-amber-500 mt-2 block">${analytics.revenue}.00</span>
                </div>
                <div className="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-500 block">Active Bookings Pipeline</span>
                  <span className="text-3xl font-black text-white mt-2 block">{analytics.totalBookings}</span>
                </div>
                <div className="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-500 block">Total Monitored Fleet</span>
                  <span className="text-3xl font-black text-white mt-2 block">{analytics.activeFleet} Units</span>
                </div>
              </div>

              {/* FLEET CONTROL UTILITY */}
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">
                <h3 className="text-sm font-bold uppercase tracking-wider text-slate-400 mb-4">Internal Fleet Status Control</h3>
                <div className="overflow-x-auto">
                  <table className="w-full text-left text-xs border-collapse">
                    <thead>
                      <tr className="border-b border-slate-800 text-slate-500 uppercase tracking-wider">
                        <th className="pb-3 font-semibold">Vehicle Asset</th>
                        <th className="pb-3 font-semibold">Class Group</th>
                        <th className="pb-3 font-semibold">Base Cost/Day</th>
                        <th className="pb-3 font-semibold">Active Pipeline State</th>
                        <th className="pb-3 font-semibold text-right">Administrative Override</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-800/50">
                      {vehicles.map(v => (
                        <tr key={v.id} className="group">
                          <td className="py-3 font-bold text-white">{v.brand} {v.model}</td>
                          <td className="py-3 text-slate-400">{v.category}</td>
                          <td className="py-3 text-slate-400 font-mono">${v.pricePerDay}</td>
                          <td className="py-3">
                            <span className={`px-2 py-0.5 rounded text-[10px] uppercase font-bold tracking-tight ${v.status === 'Available' ? 'bg-emerald-500/10 text-emerald-400' : 'bg-rose-500/10 text-rose-400'}`}>
                              {v.status}
                            </span>
                          </td>
                          <td className="py-3 text-right">
                            <button 
                              onClick={() => {
                                const updated = vehicles.map(item => item.id === v.id ? { ...item, status: item.status === 'Available' ? 'Maintenance' : 'Available' } : item);
                                setVehicles(updated);
                              }}
                              className="text-amber-500 font-semibold hover:underline bg-transparent border-none cursor-pointer"
                            >
                              Toggle State
                            </button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </main>

      {/* ==========================================
          4. MULTI-STEP BOOKING WORKFLOW ENGINE (MODAL DRAWER)
         ========================================== */}
      <AnimatePresence>
        {selectedVehicle && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
            
            {/* Backdrop Blur Overlays */}
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} onClick={() => { if(!isSubmitting) setSelectedVehicle(null); }} className="absolute inset-0 bg-black/80 backdrop-blur-sm" />

            {/* Modal Surface Block */}
            <motion.div variants={modalVariants} initial="hidden" animate="visible" exit="exit" className="bg-slate-900 border border-slate-800 rounded-3xl w-full max-w-xl overflow-hidden shadow-2xl relative z-10 flex flex-col max-h-[90vh]">
              
              {/* Header Context Banner */}
              <div className="p-6 border-b border-slate-800 flex justify-between items-start bg-slate-950">
                <div>
                  <span className="text-[10px] font-mono tracking-widest text-amber-500 uppercase">Interactive Booking Pipeline</span>
                  <h3 className="text-xl font-black text-white mt-1">{selectedVehicle.brand} {selectedVehicle.model}</h3>
                </div>
                <button disabled={isSubmitting} onClick={() => setSelectedVehicle(null)} className="w-8 h-8 rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-400 hover:text-white disabled:opacity-50">✕</button>
              </div>

              {/* Progress Flow Stepper Indicator */}
              <div className="px-6 py-3 bg-slate-900/50 border-b border-slate-800 flex items-center gap-4 text-xs font-semibold text-slate-400">
                <span className={bookingStep >= 1 ? "text-amber-500 font-bold" : ""}>1. Parameters</span>
                <span className="text-slate-700">➔</span>
                <span className={bookingStep >= 2 ? "text-amber-500 font-bold" : ""}>2. Options</span>
                <span className="text-slate-700">➔</span>
                <span className={bookingStep === 3 ? "text-amber-500 font-bold" : ""}>3. Authorization</span>
              </div>

              {/* Interactive Steps Form Fields Content Container */}
              <div className="p-6 overflow-y-auto flex-1">
                <AnimatePresence mode="wait">
                  
                  {bookingStep === 1 && (
                    <motion.div key="step1" initial={{ opacity: 0, x: 10 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -10 }} className="space-y-4">
                      <div>
                        <label className="block text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Logistical Pickup Depot Node</label>
                        <select value={formData.pickup} onChange={(e) => setFormData({...formData, pickup: e.target.value})} className="w-full bg-slate-950 border border-slate-800 rounded-xl p-3 text-sm text-white focus:outline-none focus:border-amber-500">
                          <option value="Los Angeles">Los Angeles Depot (LAX)</option>
                          <option value="Miami">Miami International Beach Terminal</option>
                          <option value="New York">New York JFK Core Hub</option>
                        </select>
                      </div>
                      <div>
                        <label className="block text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Duration Allocation (Days)</label>
                        <input type="number" min="1" max="30" value={formData.days} onChange={(e) => setFormData({...formData, days: parseInt(e.target.value) || 1})} className="w-full bg-slate-950 border border-slate-800 rounded-xl p-3 text-sm text-white focus:outline-none focus:border-amber-500 font-mono" />
                      </div>
                    </motion.div>
                  )}

                  {bookingStep === 2 && (
                    <motion.div key="step2" initial={{ opacity: 0, x: 10 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -10 }} className="space-y-4">
                      <div onClick={() => setFormData({...formData, insurance: !formData.insurance})} className={`p-4 rounded-xl border transition-all cursor-pointer flex items-center justify-between ${formData.insurance ? 'bg-amber-500/10 border-amber-500/40 text-white' : 'bg-slate-950 border-slate-800 text-slate-400'}`}>
                        <div>
                          <h4 className="text-sm font-bold">Zero-Deductible Enterprise Collision Liability Cover</h4>
                          <p className="text-xs text-slate-500 mt-1">Guarantees comprehensive mitigation protection against telemetry or collision incidents.</p>
                        </div>
                        <div className="font-mono text-sm font-bold whitespace-nowrap ml-4">+$25 / day</div>
                      </div>
                    </motion.div>
                  )}

                  {bookingStep === 3 && (
                    <motion.div key="step3" initial={{ opacity: 0, x: 10 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -10 }} className="text-center py-6 space-y-4">
                      {isSuccess ? (
                        <div className="space-y-2">
                          <div className="w-12 h-12 bg-emerald-500/20 text-emerald-400 rounded-full flex items-center justify-center mx-auto text-xl font-bold">✓</div>
                          <h4 className="text-lg font-bold text-white">Payment Securely Processed</h4>
                          <p className="text-xs text-slate-400">Database booking verification generated. Confirmation email dispatched via API.</p>
                        </div>
                      ) : (
                        <div className="text-left bg-slate-950 border border-slate-800 rounded-2xl p-4 space-y-3">
                          <h4 className="text-xs uppercase font-mono text-slate-500 tracking-wider">Final Structural Cost Allocation Breakdown</h4>
                          <div className="flex justify-between text-sm text-slate-300">
                            <span>{selectedVehicle.brand} {selectedVehicle.model} ({formData.days} Days)</span>
                            <span className="font-mono">${selectedVehicle.pricePerDay * formData.days}</span>
                          </div>
                          {formData.insurance && (
                            <div className="flex justify-between text-sm text-slate-300">
                              <span>Collision Insurance Umbrella Block</span>
                              <span className="font-mono">${25 * formData.days}</span>
                            </div>
                          )}
                          <div className="border-t border-slate-800 pt-3 flex justify-between text-base font-black text-white">
                            <span>Aggregate Authorized Total</span>
                            <span className="font-mono text-amber-500">${(selectedVehicle.pricePerDay * formData.days) + (formData.insurance ? 25 * formData.days : 0)}</span>
                          </div>
                        </div>
                      )}
                    </motion.div>
                  )}

                </AnimatePresence>
              </div>

              {/* Action Sheet Execution Bar */}
              {!isSuccess && (
                <div className="p-4 bg-slate-950 border-t border-slate-800 flex justify-between gap-4">
                  <button 
                    disabled={bookingStep === 1 || isSubmitting} 
                    onClick={() => setBookingStep(p => p - 1)} 
                    className="px-4 py-2 text-xs font-bold border border-slate-800 text-slate-400 hover:text-white rounded-xl disabled:opacity-30"
                  >
                    Back
                  </button>
                  
                  {bookingStep < 3 ? (
                    <button onClick={() => setBookingStep(p => p + 1)} className="px-5 py-2 text-xs font-bold bg-slate-100 text-black hover:bg-white rounded-xl">Continue Pipeline</button>
                  ) : (
                    <button 
                      disabled={isSubmitting} 
                      onClick={handleExecuteBooking}
                      className="px-6 py-2 text-xs font-bold bg-amber-500 hover:bg-amber-400 text-black rounded-xl disabled:opacity-50 flex items-center gap-2"
                    >
                      {isSubmitting ? "Processing Transaction..." : "Authorize Sandbox Checkout"}
                    </button>
                  )}
                </div>
              )}

            </motion.div>
          </div>
        )}
      </AnimatePresence>

    </div>
  );
}'''