| Function                                | Category                   |
|-----------------------------------------|----------------------------|
| ret_from_fork                           | Init ksoftirqd             |
| kthread                                 | Init ksoftirqd             |
| smp_boot_thread_fn                      | Init ksoftirqd             |
| run_ksoftirqd                           | Init ksoftirqd             |
| ret_from_fork                           | Init RX-IRQ/Init TX-IRQ    |
| kthread                                 | Init RX-IRQ/Init TX-IRQ    |
| irq_thread                              | Init RX-IRQ/Init TX-IRQ    |
| irq_thread_fn                           | Init RX-IRQ/Init TX-IRQ    |
| iwl_pcie_irq_rx_msix_handler            | Init RX-IRQ/Init TX-IRQ    |
| __local_bh_enable_ip                    | Init RX-IRQ/Init TX-IRQ    |
| do_softirq                              | Init RX-IRQ/Init TX-IRQ    |
| do_softirq_iown_stack                   | Init RX-IRQ/Init TX-IRQ    |
| call_on_irq_stack                       | Init RX-IRQ/Init TX-IRQ    |
| ____do_softirq                          | Init RX-IRQ/Init TX-IRQ    |
| el1h_64_irq                             | Init RX-IRQ/Init TX-IRQ    |
| el1h_64_irq_handler                     | Init RX-IRQ/Init TX-IRQ    |
| irq_exit_rcu                            | Init RX-IRQ/Init TX-IRQ    |
| ip_list_rcv                             | IP Stack                   |
| ip_sublist_rcv                          | IP Stack                   |
| ip_sublist_rcv_finish                   | IP Stack                   |
| ip_forward                              | IP Stack                   |
| ip_forward_finish                       | IP Stack                   |
| ip_output                               | IP Stack                   |
| ip_finish_output                        | IP Stack                   |
| __ip_finish_output                      | IP Stack                   |
| ip_finish_output_2                      | IP Stack                   |
| bcmgenet_rx_poll                        | Poll Function              |
| bcmgenet_tx_poll                        | Poll Function              |
| bcmgenet_rx_refill                      | Poll Function              |
| iwl_pcie_napi_poll_msix                 | Poll Function              |
| iwl_pcie_rx_handle                      | Poll Function              |
| iwl_mvm_rx_mq                           | Poll Function              |
| iwl_mvm_rx_common                       | Poll Function              |
| iwl_mvm_rx_ba_notif                     | Poll Function              |
| do_softirq_own_stack                    | RX SoftIRQ/TX SoftIRQ      |
| call_on_irq_stack                       | RX SoftIRQ/TX SoftIRQ      |
| ___do_softirq                           | RX SoftIRQ/TX SoftIRQ      |
| __do_softirq                            | RX SoftIRQ/TX SoftIRQ      |
| net_rx_action                           | RX SoftIRQ/TX SoftIRQ      |
| net_tx_action                           | RX SoftIRQ/TX SoftIRQ      |
| __napi_poll.constprop.0                 | RX SoftIRQ/TX SoftIRQ      |
| netif_receive_skb_list_internal         | RX SoftIRQ/TX SoftIRQ      |
| __netif_receive_skb_list_core           | RX SoftIRQ/TX SoftIRQ      |
| napi_gro_receive                        | RX SoftIRQ/TX SoftIRQ      |
| napi_complete_done                      | RX SoftIRQ/TX SoftIRQ      |
| __dev_queue_xmit                        | TX qdisc                   |
| __qdisc_run                             | TX qdisc                   |
| sch_direct_xmit                         | TX qdisc                   |
| net_tx_action                           | TX qdisc                   |
| dev_hard_start_xmit                     | TX qdisc                   |
| __qdisc_run                             | TX qdisc                   |
| net_tx_action                           | TX qdisc                   |
| dev_hard_start_smit                     | TX qdisc                   |
| bcmgenet_free_tx_cb                     | TX Reclaim                 |
| __bcmgenet_tx_reclaim                   | TX Reclaim                 |
| iwl_mvm_tx_reclaim                      | TX Reclaim                 |
| iwl_txq_reclaim                         | TX Reclaim                 |
| iwl_txq_free_tfd                        | TX Reclaim                 |
| iwl_txq_gen2_tfd_unmap                  | TX Reclaim                 |
| iwl_txq_gen2_set_tb                     | TX Reclaim                 |
| iwl_pcie_rxq_restock                    | TX Reclaim                 |
| iwl_pcie_rxmq_restock.part.0            | TX Reclaim                 |
| ieee80211_tx_status                     | TX Reclaim                 |
| ieee80211_tx_status_ext                 | TX Reclaim                 |
| consume_skb                             | TX Reclaim                 |
| skb_release_data                        | TX Reclaim                 |
| sta_info_get_by_addrs                   | TX Reclaim                 |
| ieee80211_report_used_skb               | TX Reclaim                 |
| ieee80211_sta_tx_notify                 | TX Reclaim                 |
| kmem_cache_free                         | TX Reclaim                 |
| __slab_free                             | TX Reclaim                 |
| put_cpu_partial                         | TX Reclaim                 |
| slab_update_freelist.constprop.0.isra.0 | TX Reclaim                 |
| raw_spin_unlock_bc                      | TX Reclaim                 |
| __dev_queue_xmit                        | Xmit                       |
| _raw_spin_unlock                        | Xmit                       |
| vprintk_store                           | Xmit                       |
| ___slab_alloc                           | Xmit                       |
| arch_sync_dma_for_device                | Xmit                       |
| __memmove                               | Xmit                       |
| dcache_inval_poc                        | Xmit                       |
| __local_bh_disable_ip                   | Xmit                       |
| console_unlock                          | Xmit                       |
| __down_trylock_console_sem.constprop.0  | Xmit                       |
| bcmgenet_xmit                           | Xmit                       |
| ieee80211_rx_list                       | Xmit                       |
| ieee80211_rx_8023                       | Xmit                       |
| kmem_cache_alloc_node                   | Xmit                       |
| __update_cpu_freelist_fast              | Xmit                       |
| ieee80211_prepare_and_rx_handle         | Xmit                       |
| _raw_spin_lock                          | Xmit                       |
| iwl_mvm_rx_fill_status                  | Xmit                       |
| __skb_flow_dissect                      | Xmit                       |
| __netif_receive_skb_core.constprop.0    | Xmit                       |
| queue_work_on                           | Xmit                       |
| _raw_spin_unlock_irqrestore             | Xmit                       |
| __kmem_cache_alloc_node                 | Xmit                       |
| __siphash_unaligned                     | Xmit                       |
| skb_copy_bits                           | Xmit                       |
| fq_codel_dequeue                        | Xmit                       |
| arch_counter_get_cntpct                 | Xmit                       |
| arch_sync_dma_for_cpu                   | Xmit                       |
| __alloc_skb                             | Xmit                       |
| iwl_pcie_rxmq_restock.part.0            | Xmit                       |
| dma_map_page_attrs                      | Xmit                       |
| iwl_fw_lookup_notif_ver                 | Xmit                       |
| __iwl_dbg                               | Xmit                       |
| dcache_clean_poc                        | Xmit                       |
| dma_unmap_page_attrs                    | Xmit                       |
| ip_rcv_core                             | Xmit                       |
| __pi_memcmp                             | Xmit                       |
| __qdisc_run                             | Xmit                       |
| __pi_memset                             | Xmit                       |
| kmem_cache_free                         | Xmit                       |
| __free_pages                            | Xmit                       |
| __build_skb_around                      | Xmit                       |
| queued_spin_lock_slowpath               | Xmit                       |
| _raw_spin_lock_bh                       | Xmit                       |
| ip_route_input_slow                     | Xmit                       |
| pskb_expand_head                        | Xmit                       |
| ip_rcv_finish_core.constprop.0          | Xmit                       |
| bsearch                                 | Xmit                       |
| kmalloc_reserve                         | Xmit                       |
| skb_put                                 | Xmit                       |
| _prb_read_valid                         | Xmit                       |
| dev_gro_receive                         | Xmit                       |
| kmalloc_slab                            | Xmit                       |
| do_csum                                 | Xmit                       |
| queue_delayed_work_on                   | Xmit                       |
| qdisc_maybe_clear_missed                | Xmit                       |
| rs_update_last_rssi                     | Xmit                       |
| __rcu_read_unlock                       | Xmit                       |
| fib_table_lookup                        | Xmit                       |
| ieee80211_channel_to_freq_khz           | Xmit                       |
| sch_direct_xmit                         | Xmit                       |
| iwl_get_cmd_string                      | Xmit                       |
| finish_task_switch.isra.0               | Xmit                       |
| __pskb_pull_tail                        | Xmit                       |
| ip_skb_dst_mtu                          | Xmit                       |
| csum_partial                            | Xmit                       |
| ktime_get_with_offset                   | Xmit                       |
| ieee80211_hdrlen                        | Xmit                       |
| dev_hard_start_xmit                     | Xmit                       |
| fq_codel_enqueue                        | Xmit                       |
| skb_free_head                           | Xmit                       |
| skb_pull                                | Xmit                       |
| iwl_hcmd_names_cmp                      | Xmit                       |
| __srcu_read_lock                        | Xmit                       |
| __srcu_read_unlock                      | Xmit                       |
| console_flush_all.constprop.0           | Xmit                       |
| desc_read_finalized_seq                 | Xmit                       |
| ip_route_use_hint                       | Xmit                       |
| validate_xmit_skb                       | Xmit                       |
| ieee80211_rx_data_set_sta               | Xmit                       |
| __rcu_read_lock                         | Xmit                       |
| iwl_pcie_rx_reuse_rbd                   | Xmit                       |
| ktime_get                               | Xmit                       |
| ieee80211_rx_mesh_data                  | Xmit                       |
| ieee80211_deliver_skb_to_local_stack    | Xmit                       |
| netdev_core_pick_tx                     | Xmit                       |
| udp_v4_early_demux                      | Xmit                       |
| __skb_get_hash                          | Xmit                       |
| netif_skb_features                      | Xmit                       |
| __napi_schedule                         | Xmit                       |
| ieee80211_clean_skb                     | Xmit                       |
| skb_push                                | Xmit                       |
| skb_network_protocol                    | Xmit                       |
| kmalloc_size_roundup                    | Xmit                       |
| eth_type_trans                          | Xmit                       |
| __skb_flow_get_ports                    | Xmit                       |
| validate_xmit_xfrm                      | Xmit                       |
| fib_validate_source                     | Xmit                       |
| sta_stats_encode_rate                   | Xmit                       |
| validate_xmit_skb_list                  | Xmit                       |
| _raw_spin_unlock_bh                     | Xmit                       |
| __kmalloc_node_track_caller             | Xmit                       |
| __wake_up_klogd.part.0                  | Xmit                       |
| fib_lookup_good_nhc                     | Xmit                       |
| new_slab                                | Xmit                       |
| dev_qdisc_enqueue                       | Xmit                       |
| printk_get_next_message                 | Xmit                       |
| memcg_slab_post_alloc_hook              | Xmit                       |
| should_failslab                         | Xmit                       |
| skb_add_rx_frag                         | Xmit                       |
| map_id_range_down                       | Xmit                       |
| __slab_alloc.constprop.0                | Xmit                       |
| irq_work_claim                          | Xmit                       |
| get_page_from_freelist                  | Xmit                       |
| arch_counter_read                       | Xmit                       |
| skb_headers_offset_update               | Xmit                       |
| dequeue_func                            | Xmit                       |
| ip_route_input_noref                    | Xmit                       |
| prb_read_valid                          | Xmit                       |
| skb_defer_rx_timestamp                  | Xmit                       |
| get_data                                | Xmit                       |
| neigh_resolve_output                    | Xmit                       |
| __alloc_pages                           | Xmit                       |
| iwl_mvm_sta_fw_id_mask                  | Xmit                       |
| console_trylock                         | Xmit                       |
| wake_threads_waitq                      | Xmit                       |
| __schedule                              | Xmit                       |
| iwl_mvm_release_frames                  | Xmit                       |
| make_kuid                               | Xmit                       |
| dev_requeue_skb                         | Xmit                       |
| vprintk_default                         | Xmit                       |
| schedule                                | Xmit                       |
| iwl_pcie_rxq_restock                    | Xmit                       |
| __wake_up                               | Xmit                       |
| __wake_up_common_lock                   | Xmit                       |
| __local_bh_enable_ip                    | Xmit                       |
