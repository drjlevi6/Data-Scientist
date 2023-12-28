# There must be links to these files in a folder included in sys.path!
import debates_array, debates_indexed, debates_sorted
import debates_stripped, debates_displayed
import debates_with_sigmoids #import Debates_with_sigmoids

ar = debates_array.Debates_array(n_candidates=4, n_debates=5)
ar.print()

pd_idx = debates_indexed.Debates_indexed(ar)
pd_idx.print()

pd_sorted = debates_sorted.Debates_sorted(pd_idx)
pd_sorted.print()

pd_strip = debates_stripped.Debates_stripped(pd_sorted)
pd_strip.print()

debates_displayed.Debates_displayed(pd_strip)

pd_sig = debates_with_sigmoids.Debates_with_sigmoids(pd_strip, linewidth=10)
pd_sig.show()
print("\n__main__ completed.")